import sys
import subprocess
import shutil

TIMEOUT_INTERVAL = 10


def parse_config(filename):
    with open(filename) as f:
        return map(
            lambda l: l + ["80"] if len(l) == 1 else l,
            map(lambda s: s.split(), filter(lambda s: s.strip() != "", f.readlines())),
        )


def check_args():
    assert len(sys.argv) == 3  # USAGE: python3 main.py <server file> <http test file>


def main():
    _, serverlist_filename, http_filename = sys.argv

    servers = parse_config(serverlist_filename)

    procs = [
        subprocess.Popen(
            [shutil.which("nc"), server, port],
            stdin=open(http_filename),
            stdout=subprocess.PIPE,
        )
        for server, port in servers
    ]

    print(*[proc.stdout.read() for proc in procs])


if __name__ == "__main__":
    check_args()
    main()
