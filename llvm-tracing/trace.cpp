#include "trace.hpp"
#include <llvm/IR/BasicBlock.h>   // for BasicBlock
#include <llvm/IR/DerivedTypes.h> // for FunctionType
#include <llvm/IR/Function.h>     // for Function
#include <llvm/IR/IRBuilder.h>    // for IRBuilder
#include <llvm/IR/Instructions.h> // for CallInst
#include <llvm/IR/Module.h>       // for Module

std::string create_unique_block_label(llvm::BasicBlock &block) {
    llvm::Module *mod = block.getParent()->getParent();
    llvm::Function *function = block.getParent();
    std::string result(std::string(mod->getName()) + "_" + std::string(function->getName()));
    llvm::raw_string_ostream rsos(result);
    block.printAsOperand(rsos, false);
    result += "\n";

    return result;
}

llvm::Constant *TracePass::create_global_gep(llvm::IRBuilder<> &builder, llvm::BasicBlock &block, std::string str) {
    llvm::GlobalVariable *global = builder.CreateGlobalString(str);
    llvm::Constant *gep = llvm::ConstantExpr::getGetElementPtr(global->getValueType(), global,
                                                               /*indices=*/{i32_zero, i32_zero},
                                                               /*inBounds=*/true);
    return gep;
}

void TracePass::handle_function(llvm::Function &function) {
    llvm::LLVMContext &context = function.getContext();

    i32_llvm_type = llvm::IntegerType::getInt32Ty(context);
    i8_llvm_type = llvm::IntegerType::getInt8Ty(context);
    i8_ptr_llvm_type = llvm::PointerType::getUnqual(i8_llvm_type);

    // In glibc, FILE is just a typedef for _IO_FILE.
    file_llvm_type = llvm::StructType::create(context, "struct._IO_FILE");
    file_ptr_llvm_type = llvm::PointerType::getUnqual(file_llvm_type);

    i32_zero = llvm::Constant::getNullValue(i32_llvm_type);

    llvm::FunctionType *fopen_type = llvm::FunctionType::get(file_ptr_llvm_type, {i8_ptr_llvm_type, i8_ptr_llvm_type}, /*isVarArg=*/false);
    llvm::FunctionType *fputs_type = llvm::FunctionType::get(i32_llvm_type, {i8_ptr_llvm_type, file_ptr_llvm_type}, /*isVarArg=*/false);
    llvm::FunctionType *fclose_type = llvm::FunctionType::get(i32_llvm_type, {file_ptr_llvm_type}, /*isVarArg=*/false);

    llvm::FunctionCallee fopen_fn = mod->getOrInsertFunction("fopen", fopen_type);
    llvm::FunctionCallee fputs_fn = mod->getOrInsertFunction("fputs", fputs_type);
    // llvm::FunctionCallee fflush_fn = mod->getOrInsertFunction("fflush", fclose_type); // fflush and fclose have the same fn signature.
    llvm::FunctionCallee fclose_fn = mod->getOrInsertFunction("fclose", fclose_type);

    std::string mode_flags("a");
    std::string log_filename("/tmp/tracer_log.out");

    for (llvm::BasicBlock &block : function) {
        llvm::IRBuilder builder(&block);
        llvm::BasicBlock::iterator insertion_pt = block.getFirstInsertionPt();

        llvm::CallInst *fopen_call =
            llvm::CallInst::Create(fopen_fn, {create_global_gep(builder, block, log_filename), create_global_gep(builder, block, mode_flags)});
        fopen_call->insertBefore(&*insertion_pt);

        llvm::CallInst *fputs_call =
            llvm::CallInst::Create(fputs_fn, {create_global_gep(builder, block, create_unique_block_label(block)), fopen_call});
        fputs_call->insertAfter(fopen_call);

        // llvm::CallInst *fflush_call = llvm::CallInst::Create(fflush_fn, {fopen_call});
        // fflush_call->insertAfter(fputs_call);

        llvm::CallInst *fclose_call = llvm::CallInst::Create(fclose_fn, {fopen_call});
        fclose_call->insertAfter(fputs_call);
    }
}

bool TracePass::runOnModule(llvm::Module &mod_param) {
    mod = &mod_param;

    for (llvm::Function &function : *mod) {
        handle_function(function);
    }

    return true;
}
