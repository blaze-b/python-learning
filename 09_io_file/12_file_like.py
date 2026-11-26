from pathlib import Path
from urllib.request import urlopen

HERE = Path(__file__).resolve().parent


def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


path = HERE / "wasteland.txt"
if not path.exists():
    path.write_text(
        "What are the roots that clutch, What branches grow\n"
        "Out of this stony rubbish? Son of man,\n"
        "You cannot say, or guess, for you know only,\n"
        "A heap of broken images, where the sun beats\n",
        encoding="utf-8",
    )

with open(path, mode="rt", encoding="utf-8") as real_file:
    wpl = words_per_line(real_file)

print(wpl)

with urlopen("http://sixty-north.com/c/t.txt") as web_file:
    wpl = words_per_line(web_file)

print(wpl)

print(type(web_file))
