#include <cctype>
#include <cstdint>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

using std::int32_t;
using std::uint8_t;

bool istchar(uint8_t c) {
    return std::isalnum(c) || c == '!' || c == '#' || c == '$' || c == '%' || c == '&' || c == '\'' || c == '*' || c == '+' || c == '-' || c == '.' ||
           c == '^' || c == '_' || c == '`' || c == '|' || c == '~';
}

bool isvchar(uint8_t c) {
    return 0x21 <= c && c <= 0x7e;
}

bool isobstext(uint8_t c) {
    return 0x80 <= c; // all chars are <= 0xff, so no need to verify that.
}

bool isfieldvchar(uint8_t c) {
    return isvchar(c) || isobstext(c);
}

bool isspaceortab(uint8_t c) {
    return c == ' ' || c == '\t';
}

void pass_over_ows(void) {
    // Read from stdin until we get past the OWS.
    uint8_t c;
    while (isspaceortab(std::cin.peek())) {
        c = std::cin.get();
    }
}

void parse_field_name(std::string &output_buffer) {
    // Parse a header field name from stdin.

    // Read bytes from stdin until we hit the max allowable characters or we read
    // something that isn't a tchar.
    while (istchar(std::cin.peek())) {
        output_buffer.push_back(std::cin.get());
    }

    // If we stopped on anything other than a colon, there must have been a
    // non-tchar in the header name
    if (std::cin.get() != ':') {
        fputs("Invalid character in HTTP header!\n", stderr);
        exit(1);
    }
}

void parse_field_value(std::string &output_buffer) {
    // Parse an http header field value from stdin

    // A field value is a sequence of zero or more field-vchars or spaces or tabs,
    // (note that this -> a field-value can be empty) starting and ending with a
    // field-vchar. A field-vchar is defined by isfieldvchar above.

    while (isfieldvchar(std::cin.peek()) || isspaceortab(std::cin.peek())) {
        output_buffer.push_back(std::cin.get());
    }

    if (std::cin.get() != '\r' || std::cin.get() != '\n') {
        fputs("No CRLF!\n", stderr);
        exit(1);
    }

    while (!output_buffer.empty() && isspaceortab(output_buffer.back())) {
        output_buffer.pop_back();
    }
}

int main(int argc, char **argv) {
    // Parse an HTTP header

    // A field line consists of a field name
    //                            ':'
    //                            optional whitespace (spaces+tabs only)
    //                            field value
    //                            optional whitespace (spaces+tabs only)
    //                            CRLF

    // Even though the CRLF is technically not part of the field line grammar rule
    // in RFC9112, we are including it here because a CRLF actually does always follow a header field,
    // it's just specified in a different part of the grammar.

    // A field name (is defined to be a `token`, which) consists of one or more
    // tchars, which are defined by istchar above.
    std::string field_name;
    parse_field_name(field_name);

    pass_over_ows();

    std::string field_value;
    parse_field_value(field_value);
    // parse_field_value also grabs the OWS and CRLF

    std::cout << "<header_name>" << field_name << "</header_name><header_value>" << field_value << "</header_value>" << std::endl;

    return EXIT_SUCCESS;
}
