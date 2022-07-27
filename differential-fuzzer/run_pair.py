import sys
import subprocess
import random
import io
import pathlib
from typing import List, Dict, Set, FrozenSet

AFL_SHOWMAP_PATH: pathlib.PosixPath = pathlib.PosixPath("../afl-showmap")
SEED_INPUTS: List[pathlib.PosixPath] = [pathlib.PosixPath("./test.http_header")]
TRACE_DIR: pathlib.PosixPath = pathlib.PosixPath("./traces")
TIMEOUT_TIME: int = 10  # Time in seconds given to each process
FECUNDITY: int = 5  # How much each input gets to reproduce if it does a good job


def byte_flip(s: str) -> str:
    index: int = random.randint(0, len(s) - 1)
    return s[:index] + chr(random.randint(0, 255)) + s[index + 1 :]


def byte_insert(s: str) -> str:
    index: int = random.randint(0, len(s) - 1)
    return s[:index] + chr(random.randint(0, 255)) + s[index:]


def probably_byte_delete(s: str) -> str:
    if s == "":
        return byte_insert(s)

    index: int = random.randint(0, len(s) - 1)
    return s[:index] + s[index + 1 :]


def mutate_input(input_filename: pathlib.PosixPath) -> pathlib.PosixPath:
    mutant_filename: pathlib.PosixPath = pathlib.PosixPath(
        f"inputs/{random.randint(0, 2**32-1)}.input"
    )
    with open(mutant_filename, "w") as f:
        f.write(
            random.choice((byte_flip, byte_insert, probably_byte_delete))(
                open(input_filename).read()
            )
        )

    return mutant_filename


def parse_trace_file(trace_file: io.TextIOWrapper) -> Dict[int, int]:
    result: Dict[int, int] = {}
    for line in trace_file.readlines():
        edge, count = map(int, line.strip().split(":"))
        result[edge] = count
    return result


def get_trace_length(trace_file: io.TextIOWrapper) -> int:
    return sum(c for e, c in parse_trace_file(trace_file).items())


def get_trace_edge_set(trace_file: io.TextIOWrapper) -> FrozenSet[int]:
    return frozenset(e for e, c in parse_trace_file(trace_file).items())


def get_trace_filename(
    executable: pathlib.PosixPath, input_file: pathlib.PosixPath
) -> pathlib.PosixPath:
    return pathlib.PosixPath(f"traces/{executable.name}_on_{input_file.name}.trace")


def main():
    executables: List[pathlib.PosixPath] = [pathlib.PosixPath(e) for e in sys.argv[1:]]
    input_queue: List[pathlib.PosixPath] = SEED_INPUTS

    # One input `I` produces one trace per program being fuzzed.
    # Convert each trace to a (frozen)set of edges by deduplication.
    # Pack those sets together in a tuple.
    # This is a fingerprint of the programs' execution on the input `I`.
    # Keep these fingerprints in a set.
    # An input is worth mutation if its fingerprint is new.
    explored: Set[Tuple[FrozenSet[int]]] = set()

    while input_queue != []:
        current_input: pathlib.PosixPath = input_queue.pop()

        procs: List[subprocess.Popen] = [
            subprocess.Popen(
                [
                    AFL_SHOWMAP_PATH,
                    "-o",
                    get_trace_filename(executable, current_input),
                    "--",
                    executable.absolute(),
                ],
                stdin=open(current_input),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            for executable in executables
        ]

        # Give the processes time if they need it. Kill them if they don't finish in time.
        for proc in procs:
            proc.wait(TIMEOUT_TIME)

        trace_edges: Tuple[FrozenSet[int]] = tuple(
            get_trace_edge_set(open(get_trace_filename(e, current_input)))
            for e in executables
        )

        if trace_edges not in explored:
            explored.add(trace_edges)
            print(current_input.absolute())
            for _ in range(FECUNDITY):
                input_queue.append(mutate_input(current_input))


if __name__ == "__main__":
    main()
