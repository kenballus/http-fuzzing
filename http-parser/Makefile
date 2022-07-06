DAFFODIL := "/home/bkallus/downloads/apache-daffodil-3.3.0-bin/bin/daffodil"
SCHEMA := "http1_1.dfdl.xsd"
OUT_FILE := "dfdl.out"
TEST_FILE := test.http

.PHONY: all test clean
all:
	$(DAFFODIL) save-parser -s $(SCHEMA) $(OUT_FILE)

c:
	$(DAFFODIL) generate c --schema $(SCHEMA)

test:
	$(DAFFODIL) parse --schema $(SCHEMA) $(TEST_FILE)

unparse:
	$(DAFFODIL) unparse --schema $(SCHEMA) $(OUT_FILE)

clean:
	rm -rf dfdl.out c
