# Python Essential Training

Personal notes and runnable lesson scripts for core Python (3.12+).

Each numbered folder is a self-contained topic. Open the folder’s `README.md` for the longer notes that used to live here; diagrams live under [`00_images`](./00_images).

## Setup

**With venv + pip:**

```bash
python3.12 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -U pip
pip install "pytest>=8" "ruff>=0.8"
```

**With [uv](https://docs.astral.sh/uv/):**

```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install "pytest>=8" "ruff>=0.8"
# or: uv sync --group dev
```

Requires **Python 3.12+**.

## Run lessons

From the repo root (so imports like `samples.*` resolve from each script’s directory):

```bash
python 02_core/01_int.py
python 03_modularity/samples/words_extract.py http://sixty-north.com/c/t.txt
python 08_classes/04_main.py
```

Some `09_io_file` scripts write `.txt` / `.dat` / `.bmp` next to themselves; those outputs are gitignored.

## Lint, format, test

```bash
ruff check .
ruff format .
pytest
```

CI runs the same checks on Python 3.12 and 3.13, plus a gitleaks working-tree scan.

## Table of contents

| Folder | Topic |
|--------|--------|
| [00_images](./00_images) | Diagrams referenced by the notes |
| [01_fundamentals](./01_fundamentals) | REPL, references vs variables |
| [02_core](./02_core) | Scalars, conditionals, loops, strings, bytes, lists, dicts |
| [03_modularity](./03_modularity) | Modules, functions, dunders, CLI imports |
| [04_objects_types](./04_objects_types) | Object identity, argument passing, defaults, scopes |
| [05_collections](./05_collections) | Tuples, strings, ranges, lists, dicts, sets, protocols |
| [06_exceptions](./06_exceptions) | Exception flow, APIs, EAFP/LBYL, `finally` |
| [07_iterations](./07_iterations) | Comprehensions, generators, itertools |
| [08_classes](./08_classes) | Classes, polymorphism, inheritance (`air_travel`) |
| [09_io_file](./09_io_file) | Text/binary files, context managers, file-like objects |
