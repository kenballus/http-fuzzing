import subprocess
import sys

ADDRESS_SIZE = 16

def is_label(line):
                                     # 5 comes from ' <', then at least 1 character in the symbol, then '>:'
    return len(line) >= ADDRESS_SIZE + 5 and all(line[i] in b"0123456789abcdef" for i in range(ADDRESS_SIZE))

def is_log_call(line):
    return line.endswith(b"<__afl_maybe_log>")

def get_symbol(label_line):
    return label_line[18:-2]

def should_be_instrumented(symbol):
    return False

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <instrumented_binary>", file=sys.stderr)

    dump = subprocess.check_output(["objdump", "-d", sys.argv[1]])

    curr_label = None

    for line in dump.split(b"\n"):
        if is_label(line):
            curr_label = get_symbol(line)
        elif should_be_instrumented(curr_label) and is_log_call(line):



if __name__ == "__main__":
    main()