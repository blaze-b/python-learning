# Chapter 1: Fundamentals

First contact with the language: printing, built-in types, literals, reserved words, and operators.

## What You'll Learn

- How a tiny Python file runs from top to bottom
- Built-in vs user-defined types at a glance
- Literals, identifiers, and the reserved-word list
- Arithmetic, assignment, relational, and logical operators

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_sample.py](./01_sample.py) | A first `print` statement |
| [02_sample.py](./02_sample.py) | Built-in datatypes overview |
| [03_sample.py](./03_sample.py) | Literals and identifiers |
| [04_sample.py](./04_sample.py) | Reserved keywords you cannot rebind |
| [05_sample.py](./05_sample.py) | Operators (arithmetic, assignment, relational, logical) |

## Key Concepts

- Python has **named references to objects**, not “boxes” that hold values.
- The **REPL** (Read Eval Print Loop) is ideal for trying these snippets interactively.
- Identifiers must not collide with the language’s reserved words.

## How To Run

```bash
python 01_fundamentals/01_sample.py
python 01_fundamentals/05_sample.py
```

## Try It Yourself

- Change the string in `01_sample.py` and re-run it.
- In the REPL, try `type(42)`, `type(3.14)`, and `type("hi")`.
- Attempt to assign to a keyword (e.g. `for = 1`) and read the `SyntaxError`.

## Navigation

Previous: [Chapter 0: Figures](../00_images/README.md)  
Next: [Chapter 2: Core Types](../02_core/README.md)
