# Python Learning

Runnable chapter notes for core Python 3.12+ — scripts first, short explanations second.

[![CI](https://github.com/blaze-b/python-learning/actions/workflows/ci.yml/badge.svg)](https://github.com/blaze-b/python-learning/actions/workflows/ci.yml)

## Chapters

| Chapter | Title | Summary | Link |
|--------:|-------|---------|------|
| 0 | Figures | Diagrams referenced from later chapters | [00_images](./00_images) |
| 1 | Fundamentals | REPL, types, literals, keywords, operators | [01_fundamentals](./01_fundamentals) |
| 2 | Core Types | Scalars, control flow, strings, bytes, lists, dicts | [02_core](./02_core) |
| 3 | Modularity | Modules, functions, dunders, imports, CLI samples | [03_modularity](./03_modularity) |
| 4 | Objects And Types | Identity, argument passing, defaults, scopes | [04_objects_types](./04_objects_types) |
| 5 | Collections | Tuples, strings, ranges, lists, dicts, sets, protocols | [05_collections](./05_collections) |
| 6 | Exceptions | Control flow, APIs, EAFP/LBYL, `finally`, platforms | [06_exceptions](./06_exceptions) |
| 7 | Iterations | Comprehensions, generators, itertools helpers | [07_iterations](./07_iterations) |
| 8 | Classes | Flight/aircraft samples, seating, inheritance | [08_classes](./08_classes) |
| 9 | Files And I/O | Text/binary files, Recaman demos, context managers | [09_io_file](./09_io_file) |

## Repo Layout

```text
python-learning/
├── 00_images/           # Shared diagrams
├── 01_fundamentals/     # Chapter 1
├── 02_core/             # Chapter 2
├── 03_modularity/       # Chapter 3 (+ samples/)
├── 04_objects_types/    # Chapter 4 (+ samples/)
├── 05_collections/      # Chapter 5
├── 06_exceptions/       # Chapter 6 (+ samples/)
├── 07_iterations/       # Chapter 7
├── 08_classes/          # Chapter 8 (+ samples/)
├── 09_io_file/          # Chapter 9 (+ samples/)
├── tests/               # Pytest smoke + unit tests
├── pyproject.toml       # Python 3.12+, ruff, pytest
└── .github/workflows/   # CI (lint, test, gitleaks)
```

## Prerequisites

- **Python 3.12+**
- Optional: [uv](https://docs.astral.sh/uv/) for faster installs
- Network access for a few URL-fetch demos (`sixty-north.com`)

## 2-Minute Quick Start

**venv + pip**

```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -U pip
pip install "pytest>=8" "ruff>=0.8"
```

**uv**

```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install "pytest>=8" "ruff>=0.8"
```

**Run a lesson, tests, and lint**

```bash
python 02_core/01_int.py
pytest
ruff check .
ruff format --check .
```

## How To Add A New Chapter Or Lesson

1. Create a numbered folder `NN_short_name/` (next free chapter number).
2. Add `README.md` using the chapter template (title, learn list, lessons table, notes, try-it, Previous/Next).
3. Drop numbered scripts `01_….py`, `02_….py`, …; put reusable helpers under `samples/`.
4. Link the chapter from the root [Chapters](#chapters) table and update Previous/Next links on neighbours.
5. Extend `tests/test_smoke_lessons.py` if the new folder should be smoke-tested (or rely on the existing folder list once updated).
6. Run `ruff format . && ruff check . && pytest` before opening a PR.

## Conventions

- **One idea per script** — keep demos short and runnable from the repo root.
- **Numbered filenames** — `NN_topic.py` within each chapter folder.
- **Samples packages** — importable helpers live in `samples/` (e.g. `words`, `air_travel`).
- **Generated files** — `09_io_file` may write `.txt` / `.dat` / `.bmp`; those paths are gitignored.
- **No secrets** — never commit `.env`, keys, or credentials; CI runs gitleaks on the working tree.
- **Style** — ruff formats and lints; pedagogical star-imports and explicit `open` modes are allowed where the lesson needs them.
