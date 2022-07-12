import sys
import subprocess
import shutil
import xml.etree.ElementTree
import random

TIMEOUT_INTERVAL = 10
DAFFODIL_PATH = "/home/bkallus/downloads/apache-daffodil-3.3.0-bin/bin/daffodil"
SCHEMA_PATH = "../http-parser/http1_1.dfdl.xsd"

def parse_config(filename: str):
    """ Grabs the servers and ports out of the config file. Returns a collection of string pairs of the form [[server, port], ...] """
    with open(filename) as f:
        return map(
            lambda l: l + ["80"] if len(l) == 1 else l,
            map(
                lambda s: s.split()[:2],
                filter(
                    lambda s: s.strip() != "",
                    f.readlines()
                )
            )
        )

def check_args() -> None:
    assert len(sys.argv) == 3  # USAGE: python3 main.py <server file> <http test file>

def parse_http(http_filename: str) -> xml.etree.ElementTree:
    """ Uses the daffodil parser to produce an xml parse tree from the http input file. """
    proc = subprocess.Popen(
        [DAFFODIL_PATH, "parse", "--schema", SCHEMA_PATH, http_filename],
        stdout=subprocess.PIPE
    )
    return xml.etree.ElementTree.parse(proc.stdout)

def unparse_http(tree: xml.etree.ElementTree) -> str:
    return subprocess.check_output(
        [DAFFODIL_PATH, "unparse", "--schema", SCHEMA_PATH],
        input=xml.etree.ElementTree.tostring(tree.getroot())
    ).replace(b"\n", b"\r\n") # This isn't right because it will replace '\n's inside of data as well.


def byte_fuzz(tree: xml.etree.ElementTree) -> None:
    pass

def prune_fuzz(tree: xml.etree.ElementTree) -> None:
    pass

def main():
    _, serverlist_filename, http_filename = sys.argv

    servers = parse_config(serverlist_filename)

    tree = parse_http(http_filename)
    byte_fuzz(tree)

    outputs = [
        subprocess.check_output(
            [shutil.which("nc"), server, port],
            input=unparse_http(tree)
        )
        for server, port in servers
    ]

    print("\n".join(map(str, outputs)))


if __name__ == "__main__":
    check_args()
    main()
