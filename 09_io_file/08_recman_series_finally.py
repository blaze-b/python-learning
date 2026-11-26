"""Read and print an integer series."""

from pathlib import Path

HERE = Path(__file__).resolve().parent


def read_series(filename):
    f = open(filename, mode="rt", encoding="utf-8")
    try:
        return [int(line.strip()) for line in f]
    finally:
        f.close()


def main(filename):
    series = read_series(filename)
    print(series)


if __name__ == "__main__":
    path = HERE / "recman.dat"
    if not path.exists():
        path.write_text("0\n1\n3\n6\n2\n7\n13\n20\n12\n21\n", encoding="utf-8")
    main(path)
