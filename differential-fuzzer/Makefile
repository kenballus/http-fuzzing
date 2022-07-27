CC  := ../afl-clang
CXX := ../afl-clang++
CFLAGS := -g -O0
CXXFLAGS := -g -O0
STYLE := "{BasedOnStyle: llvm, AllowShortFunctionsOnASingleLine: false, IndentWidth: 4, ColumnLimit: 150, BreakBeforeBraces: Custom, BraceWrapping: {BeforeElse: true}}"

.PHONY: compile run clean show

compile: run_pair.py c_parser cpp_parser
	mypy run_pair.py
	black run_pair.py

c_parser: test.c
	clang-format -style=$(STYLE) -i test.c
	$(CC) $(CFLAGS) test.c -o c_parser

cpp_parser: test.cpp
	clang-format -style=$(STYLE) -i test.cpp
	$(CXX) $(CXXFLAGS) test.cpp -o cpp_parser

run: compile
	mkdir -p traces inputs
	python3 run_pair.py c_parser cpp_parser > good.txt

show: run
	for thing in $$(cat good.txt); do \
		diff <(./c_parser < $$thing 2>&1) <(./cpp_parser < $$thing 2>&1); \
	done

clean:
	rm -f c_parser cpp_parser traces/*.trace inputs/*.input good.txt