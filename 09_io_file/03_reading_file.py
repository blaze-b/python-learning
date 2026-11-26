import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / "wasteland.txt"

if not path.exists():
    path.write_text(
        "What are the roots that clutch, What branches grow\n"
        "Out of this stony rubbish? ",
        encoding=sys.getdefaultencoding(),
    )

f = open(path, mode="rt", encoding=sys.getdefaultencoding())

print(f)

print(f.read(32))
print(f.read())
print(f.seek(0))

print(f.readline())
print(f.readline())
print(f.readline())
print(f.seek(0))

print(f.readlines())

f.close()
