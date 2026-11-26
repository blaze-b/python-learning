# Recaman sequence

from itertools import count, islice
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sequence():
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """Write Recaman's sequence to a text file."""
    with open(filename, mode="wt", encoding="utf-8") as f:
        f.writelines(f"{r}\n" for r in islice(sequence(), num + 1))


# CMD: python 06_recman_seq_file.py
if __name__ == "__main__":
    write_sequence(filename=HERE / "recman.dat", num=1000)
