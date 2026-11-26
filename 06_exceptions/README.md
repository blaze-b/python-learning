# 06 — Exceptions

## Exception propagation

![Exception propagation](../00_images/exception_propagation.JPG)

## Programmer errors (rarely catch)

- `IndentationError`, `SyntaxError`, `NameError`
- `pass` is a no-op; exceptions should not be silently ignored

## Exceptions as API

- Prefer standard exception types
- Invalid values → `ValueError`; wrong types often left as `TypeError`
- Raise with constructors: `raise ValueError("…")`

## Protocols

- Sequences raise `IndexError` for out-of-bounds indexing
- Common types: `IndexError`, `ValueError`, `KeyError`

## LBYL vs EAFP

- **LBYL** — Look Before You Leap (check preconditions)
- **EAFP** — Easier to Ask Forgiveness than Permission (preferred “happy path”)

## Cleanup & platform specifics

- `try` / `finally` for cleanup
- Platform modules: Windows `msvcrt`; Unix `tty` / `termios`

## Scripts & samples

| Path | Notes |
|------|--------|
| `01_…` … `09_…` | Demos of catch, re-raise, raise, EAFP, `finally` |
| `samples/exception_1.py` / `exception_2.py` | Shared helpers for conversion demos |
