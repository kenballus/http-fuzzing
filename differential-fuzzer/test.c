#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define FIELD_NAME_LENGTH_LIMIT 20
#define FIELD_VALUE_LENGTH_LIMIT 100

bool istchar(uint8_t c) {
    return isalnum(c) || c == '!' || c == '#' || c == '$' || c == '%' || c == '&' || c == '\'' || c == '*' || c == '+' || c == '-' || c == '.' ||
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
    do {
        c = getc(stdin);
    } while (isspaceortab(c));
    if (!isspaceortab(c)) { // There was no whitespace, so put c back.
        ungetc(c, stdin);
    }
}

void parse_field_name(uint8_t *output_buffer) {
    // Parse a header field name from stdin.

    // Read bytes from stdin until we hit the max allowable characters or we read
    // something that isn't a tchar.
    int32_t bytes_read = 0;
    for (; bytes_read < FIELD_NAME_LENGTH_LIMIT && (bytes_read == 0 || istchar(output_buffer[bytes_read - 1])); bytes_read++) {
        output_buffer[bytes_read] = getc(stdin);
    }

    if (bytes_read == FIELD_NAME_LENGTH_LIMIT) {
        fputs("HTTP header value is too long!\n", stderr);
        exit(1);
    }

    // If we stopped on anything other than a colon, there must have been a
    // non-tchar in the header name
    if (output_buffer[bytes_read - 1] != ':') {
        fputs("Invalid character in HTTP header!\n", stderr);
        exit(1);
    }
    else {
        // Toss the colon
        output_buffer[bytes_read - 1] = '\0';
    }
}

void parse_field_value(uint8_t *output_buffer) {
    // Parse an http header field value from stdin

    // A field value is a sequence of zero or more field-vchars or spaces or tabs,
    // (note that this -> a field-value can be empty) starting and ending with a
    // field-vchar. A field-vchar is defined by isfieldvchar above.

    int32_t bytes_read = 0;
    for (; bytes_read < FIELD_VALUE_LENGTH_LIMIT &&
           (bytes_read == 0 || isfieldvchar(output_buffer[bytes_read - 1]) || isspaceortab(output_buffer[bytes_read - 1]));
         bytes_read++) {
        output_buffer[bytes_read] = getc(stdin);
    }
    if (bytes_read == FIELD_VALUE_LENGTH_LIMIT) {
        fputs("HTTP header value is too long!\n", stderr);
        exit(1);
    }

    if (getc(stdin) != '\n' && output_buffer[bytes_read - 1] != '\r') {
        fputs("No CRLF!\n", stderr);
        exit(1);
    }

    // Toss the '\r'
    output_buffer[bytes_read - 1] = '\0';
    bytes_read--;

    while (bytes_read != 0 && isspaceortab(output_buffer[bytes_read - 1])) {
        output_buffer[bytes_read - 1] = '\0';
        bytes_read--;
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
    uint8_t field_name[FIELD_NAME_LENGTH_LIMIT] = {0};
    parse_field_name(field_name);

    pass_over_ows();

    uint8_t field_value[FIELD_VALUE_LENGTH_LIMIT] = {0};
    parse_field_value(field_value);
    // parse_field_value also grabs the OWS and CRLF

    printf("<header_name>%s</header_name><header_value>%s</header_value>\n", field_name, field_value);

    return EXIT_SUCCESS;
}
