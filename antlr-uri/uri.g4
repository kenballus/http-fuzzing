/*
    ANTLR grammar for URI.
    This is a direct translation of the ABNF in RFC 3986, with additions from RFC 6874 for IPv6 Zone Identifiers.
    As such, I have tried to keep the contents and names of rules as close to those described in the RFCs as possible.
    Also included are some pieces of RFC 2234 for ALPHA, digit, and hexdig.
*/

grammar uri;

uri
    : scheme ':' hier_part ('?' query)? ('#' fragment_)?
    ;

scheme
    : ALPHA (ALPHA | digit | '+' | '-' | '.')*
    ;

hier_part
    : '//' authority path_abempty
    | path_absolute
    | path_rootless
    | path_empty
    ;

authority
    : (userinfo '@')? host (':' port)?
    ;

userinfo
    : (unreserved | pct_encoded | sub_delims | ':')*
    ;

host
    : ip_literal
    | ipv4address
    | reg_name
    ;

ip_literal
    : '[' (ipv6address | ipv6addrz | ipvfuture) ']'
    ;

ipv6address
    : h16 ':' h16 ':' h16 ':' h16 ':' h16 ':' h16 ':' ls32
    |                                                                          '::' h16 ':' h16 ':' h16 ':' h16 ':' h16 ':' ls32
    | h16?                                                                     '::' h16 ':' h16 ':' h16 ':' h16 ':' ls32
    | ((h16 ':')? h16)?                                                        '::' h16 ':' h16 ':' h16 ':' ls32
    | ((h16 ':')? (h16 ':')? h16)?                                             '::' h16 ':' h16 ':' ls32
    | ((h16 ':')? (h16 ':')? (h16 ':')? h16)?                                  '::' h16 ':' ls32
    | ((h16 ':')? (h16 ':')? (h16 ':')? (h16 ':')? h16)?                       '::' ls32
    | ((h16 ':')? (h16 ':')? (h16 ':')? (h16 ':')? (h16 ':')? h16)?            '::' h16
    | ((h16 ':')? (h16 ':')? (h16 ':')? (h16 ':')? (h16 ':')? (h16 ':')? h16)? '::'
    ;

ls32
    : h16 ':' h16
    | ipv4address
    ;

h16
    : hexdig
    | hexdig hexdig
    | hexdig hexdig hexdig
    | hexdig hexdig hexdig hexdig
    ;

ipv6addrz
    : ipv6address '%25' zoneid
    ;

zoneid
    : (unreserved | pct_encoded)?
    ;

ipvfuture
    : 'v' hexdig+ '.' (unreserved | sub_delims | ':')+
    ;

ipv4address
    : dec_octet '.' dec_octet '.' dec_octet '.' dec_octet
    ;

dec_octet
    : digit
    | digit_nz digit
    | '1' digit digit
    | '2' digit_lt_5 digit
    | '25' digit_lt_6
    ;

reg_name
    : (unreserved | pct_encoded | sub_delims)*
    ;

// It is weird that this can be empty.
port
    : digit*
    ;

path_abempty
    : ('/' segment)*
    ;

path_absolute
    : '/' (segment_nz ('/' segment)*)?
    ;

path_rootless
    : segment_nz ('/' segment)*
    ;

path_empty
    :
    ;

query
    : (pchar | '/' | '?')*
    ;

// This is the same as query, but for whatever reason it's listed twice in the RFC.
fragment_
    : (pchar | '/' | '?')*
    ;

segment
    : pchar*
    ;

segment_nz
    : pchar+
    ;

unreserved
    : ALPHA
    | digit
    | '-'
    | '.'
    | '_'
    | '~'
    ;

pchar
    : unreserved
    | pct_encoded
    | sub_delims
    | ':'
    | '@'
    ;

pct_encoded
    : '%' hexdig hexdig
    ;

sub_delims
    : '!'
    | '$'
    | '&'
    | '\''
    | '('
    | ')'
    | '*'
    | '+'
    | ','
    | ';'
    | '='
    ;

digit_nz
    : '1'
    | '2'
    | '3'
    | '4'
    | '5'
    | '6'
    | '7'
    | '8'
    | '9'
    ;

digit_lt_5
    : '0'
    | '1'
    | '2'
    | '3'
    | '4'
    ;

digit_lt_6
    : '0'
    | '1'
    | '2'
    | '3'
    | '4'
    | '5'
    ;

digit
    : '0'
    | '1'
    | '2'
    | '3'
    | '4'
    | '5'
    | '6'
    | '7'
    | '8'
    | '9'
    ;

// It is weird that this can't be lowercase
hexdig
    : digit
    | HEXALPHA
    ;

ALPHA
    : [a-z]
    | [G-Z]
    | HEXALPHA
    ;

HEXALPHA
    : [A-F]
    ;
