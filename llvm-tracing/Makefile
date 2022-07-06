PASS_NAME := trace

CXX := clang++
LLVM_CONFIG := llvm-config
CXXFLAGS := `$(LLVM_CONFIG) --cxxflags` -fPIC -Wall -g -std=c++20
STYLE := "{BasedOnStyle: llvm, AllowShortFunctionsOnASingleLine: false, IndentWidth: 4, ColumnLimit: 150, BreakBeforeBraces: Custom, BraceWrapping: {BeforeElse: true}}"

$(PASS_NAME).so: $(PASS_NAME).o
	$(CXX) $(CXXFLAGS) -shared $(PASS_NAME).o -o $(PASS_NAME).so

$(PASS_NAME).o: $(PASS_NAME).cpp $(PASS_NAME).hpp
	clang-format -i -style=$(STYLE) $^ || echo "clang-format isn't installed..."
	$(CXX) $(CXXFLAGS) -c $(PASS_NAME).cpp -o $@

.PHONY: test baseline clean

test: $(PASS_NAME).so
	rm -f /tmp/tracer_log.out
	clang -g -O -Xclang -disable-llvm-passes -S -emit-llvm test.c -o /dev/stdout | opt -enable-new-pm=0 -S -load=./$(PASS_NAME).so --trace | tee test.ll
	clang test.ll
	./a.out
	cat /tmp/tracer_log.out


baseline: $(PASS_NAME).so
	clang -g -O -Xclang -disable-llvm-passes -S -emit-llvm test.c -o /dev/stdout | tee test.ll
	clang test.ll
	./a.out

clean:
	rm -f *.so *.o a.out test.ll
