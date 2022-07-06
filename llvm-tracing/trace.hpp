#pragma once

// Change the DEBUG_TYPE define to the friendly name of your pass...for some reason?
#define DEBUG_TYPE "trace"

#include <llvm/IR/Function.h>                       // for Function
#include <llvm/IR/IRBuilder.h>                      // for IRBuilder
#include <llvm/IR/LegacyPassManager.h>              // for legacy::PassManagerBase
#include <llvm/Pass.h>                              // for ModulePass and RegisterPass
#include <llvm/Transforms/IPO/PassManagerBuilder.h> // for RegisterStandardPasses and PassManagerBuilder

struct TracePass : public llvm::ModulePass {
    llvm::Module *mod;

    llvm::Type *i32_llvm_type;
    llvm::Type *i8_llvm_type;
    llvm::Type *i8_ptr_llvm_type;

    llvm::StructType *file_llvm_type;
    llvm::PointerType *file_ptr_llvm_type;
    llvm::Value *i32_zero;

    static char ID;
    // This constructor just calls the parent class's constructor.
    TracePass() : llvm::ModulePass(ID) {
    }

    bool runOnModule(llvm::Module &);

  private:
    void handle_function(llvm::Function &);
    llvm::Constant *create_global_gep(llvm::IRBuilder<> &, llvm::BasicBlock &, std::string);
};

char TracePass::ID = 0;

static llvm::RegisterPass<TracePass> tmp("trace", "Ben's trace pass");

static llvm::RegisterStandardPasses RegisterMyPass(llvm::PassManagerBuilder::EP_EarlyAsPossible,
                                                   [](llvm::PassManagerBuilder const &, llvm::legacy::PassManagerBase &PM) {
                                                       PM.add(new TracePass());
                                                   });
