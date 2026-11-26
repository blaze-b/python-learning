import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / "wasteland.txt"

f = open(path, mode="wt", encoding=sys.getdefaultencoding())

print(f)

f.write("What are the roots that clutch, ")

f.write("What branches grow\n")

f.write("Out of this stony rubbish? ")

f.close()
