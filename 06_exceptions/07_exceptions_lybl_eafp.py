import os
from pathlib import Path

# Prefer forward slashes / pathlib so the demo works on every platform.
p = str(Path("00_images") / "dict.JPG")


def process_file(path):
    print("Processing file in progress")
    # Touch the path so EAFP can succeed when the file exists.
    if not os.path.exists(path):
        raise OSError(f"No such file as {path}")


# LBYL

if os.path.exists(p):
    process_file(p)
else:
    print(f"No such file as {p}")

# EAFP

try:
    process_file(p)
except OSError as e:
    print(f"Error: {e}")
