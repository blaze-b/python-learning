# Chapter 3: Modularity

Functions, modules, special names, and importing sample libraries from the command line.

## What You'll Learn

- Defining functions with `def` and returning values
- Module-level scripts vs reusable functions
- `__name__ == "__main__"` and other dunder names
- Named imports vs `import *`, plus a CLI word-fetch sample

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_module.py](./01_module.py) | Module-level URL fetch and print |
| [02_functions.py](./02_functions.py) | Function definitions, returns, and `None` |
| [03_ordinal_functions.py](./03_ordinal_functions.py) | Multi-argument helpers (`nth_root`) |
| [04_dunder.py](./04_dunder.py) | Guarding execution with `__name__` |
| [05_cli_import.py](./05_cli_import.py) | Explicit named imports from `samples.words` |
| [06_cli_import.py](./06_cli_import.py) | Star-import style (`from … import *`) |
| [07_cli_import.py](./07_cli_import.py) | Calling `words_extract.main(url)` |
| [samples/words.py](./samples/words.py) | Reusable `fetch_words` / `print_words` / `main` |
| [samples/words_extract.py](./samples/words_extract.py) | CLI entry point that requires a URL argument |

## Key Concepts

### Functions

- Arguments are passed by **object reference** (references are copied, not objects).
- PEP 8 suggests two blank lines between top-level functions.

### Dunder Names

- Names like `__name__` are pronounced “dunder name” (double underscore).

### Python Execution Model

![Python Execution Model](../00_images/python_execution_model.JPG)

### Docstrings And Shebangs

- Docstrings must be the first statement in a module/function/class (PEP 257).
- Shebang (`#!`) makes a script executable: `chmod +x samples/words_extract.py`.

## How To Run

```bash
python 03_modularity/02_functions.py
python 03_modularity/samples/words.py
python 03_modularity/samples/words_extract.py http://sixty-north.com/c/t.txt
```

## Try It Yourself

- Add a docstring to `square` in `02_functions.py` and inspect it with `help(square)`.
- Refactor `01_module.py` so the fetch logic lives in a function behind `if __name__ == "__main__"`.
- Point `words_extract.py` at a `file://` URL of a local text file.

## Navigation

Previous: [Chapter 2: Core Types](../02_core/README.md)  
Next: [Chapter 4: Objects And Types](../04_objects_types/README.md)
