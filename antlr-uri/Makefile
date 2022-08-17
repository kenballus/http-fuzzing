.PHONY: all clean run

all:
	antlr4 uri.g4
	javac -cp '/usr/share/java/antlr-4.10.1-complete.jar' *.java

run:
	grun uri uri test.uri

clean:
	rm -f *.tokens *.java *.class *.interp
