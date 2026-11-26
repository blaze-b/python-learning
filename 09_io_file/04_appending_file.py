import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE / "wasteland.txt"

f = open(path, mode="at", encoding=sys.getdefaultencoding())

f.writelines(
    [
        "Son of man,\n",
        "You cannot say, or guess, ",
        "for you know only,\n",
        "A heap of broken images, ",
        "where the sun beats\n",
    ]
)

f.close()
