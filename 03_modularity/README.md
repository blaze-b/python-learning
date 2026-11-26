# 03 — Modularity

## Functions

- Defined with `def`
- Arguments are passed by **object reference** (references are copied, not the objects)
- PEP 8 recommends two blank lines between top-level functions

## Naming special functions (dunder)

- Names like `__name__` are pronounced “dunder name” (double underscore)

## Python execution model

![Python execution model](../00_images/python_execution_model.JPG)

## Docstrings

- Literal strings that document functions, modules, and classes
- Must be the first statement in the block
- Convention: PEP 257

## Shebangs

- `#!` marks an executable script
- Example: `chmod +x words_extract.py`
  - Windows: `python words_extract.py http://sixty-north.com/c/t.txt`
  - Linux: `./words_extract.py http://sixty-north.com/c/t.txt`

## Scripts & samples

| Path | Notes |
|------|--------|
| `01_module.py` | Module-level URL fetch |
| `02_functions.py` | Function basics |
| `03_ordinal_functions.py` | Ordinal helpers |
| `04_dunder.py` | `__name__ == "__main__"` |
| `05_cli_import.py` … `07_cli_import.py` | Import styles |
| `samples/words.py` | Fetch & print words from a URL |
| `samples/words_extract.py` | CLI: `python samples/words_extract.py <url>` |
