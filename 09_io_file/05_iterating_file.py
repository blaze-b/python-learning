import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
f = None


def read_file_details(path):
    opened = open(path, mode="rt", encoding=sys.getdefaultencoding())
    for line in opened:
        sys.stdout.write(line)
    return opened


try:
    f = read_file_details(sys.argv[1])
except (IndexError, NameError, FileNotFoundError) as e:
    print(e, file=sys.stderr)
    path = HERE / "wasteland.txt"
    if not path.exists():
        path.write_text("demo line one\ndemo line two\n", encoding="utf-8")
    f = read_file_details(path)
finally:
    if f is not None:
        f.close()
