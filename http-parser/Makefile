DAFFODIL := "/home/bkallus/downloads/apache-daffodil-3.3.0-bin/bin/daffodil"
SCHEMA := "http1_1.dfdl.xsd"
OUT_FILE := "dfdl.out"
TEST_FILE := test.http

.PHONY: test unparse clean
c:
	$(DAFFODIL) generate c --schema $(SCHEMA)

parse:
	$(DAFFODIL) parse --schema $(SCHEMA) $(TEST_FILE)

unparse:
	$(DAFFODIL) unparse --schema $(SCHEMA) $(OUT_FILE)

clean:
	rm -rf dfdl.out c
