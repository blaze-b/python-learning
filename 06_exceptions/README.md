# Chapter 6: Exceptions

Signalling failure, documenting APIs with exceptions, and cleaning up with `finally`.

## What You'll Learn

- Catching, logging, and re-raising errors
- Using standard exception types as part of an API
- Index/Key/Value protocol expectations
- LBYL vs EAFP styles
- Platform-specific imports with graceful fallback

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_exceptions_and_control_flows.py](./01_exceptions_and_control_flows.py) | Conversion helpers with progressive error handling |
| [02_exceptions_re_raising.py](./02_exceptions_re_raising.py) | Logging then re-raising `KeyError` |
| [03_exceptions_as_api.py](./03_exceptions_as_api.py) | Documenting failure modes for `sqrt` |
| [04_exceptions_raise.py](./04_exceptions_raise.py) | Raising `ValueError` for invalid input |
| [05_exceptions_protocols.py](./05_exceptions_protocols.py) | `IndexError`, `ValueError`, and `KeyError` demos |
| [06_exceptions_avoid_explicit_types.py](./06_exceptions_avoid_explicit_types.py) | Guarding with `TypeError` then converting |
| [07_exceptions_lybl_eafp.py](./07_exceptions_lybl_eafp.py) | Look Before You Leap vs EAFP file checks |
| [08_exceptions_finally.py](./08_exceptions_finally.py) | Cleanup with `try` / `finally` |
| [09_exceptions_platform_specific.py](./09_exceptions_platform_specific.py) | Optional platform modules |
| [samples/exception_1.py](./samples/exception_1.py) | Shared conversion helpers (`convert`, `convert_1`…) |
| [samples/exception_2.py](./samples/exception_2.py) | Conversion helper that re-raises after logging |

## Key Concepts

### Exception Propagation

![Exception Propagation](../00_images/exception_propagation.JPG)

- Programmer errors (`SyntaxError`, `IndentationError`, `NameError`) are rarely worth catching.
- Prefer standard types: `ValueError`, `TypeError`, `KeyError`, `IndexError`.

### LBYL Vs EAFP

- **LBYL** — check preconditions first.
- **EAFP** — try the happy path and handle failure (usually preferred in Python).

### Cleanup

- `try` / `finally` (or `with`) ensures resources close even when errors escape.

## How To Run

```bash
python 06_exceptions/01_exceptions_and_control_flows.py
python 06_exceptions/05_exceptions_protocols.py
python 06_exceptions/07_exceptions_lybl_eafp.py
```

## Try It Yourself

- Wrap a division helper that raises `ZeroDivisionError` and recovers with a default.
- Rewrite an LBYL file check in EAFP style using `try` / `except OSError`.
- Add a `finally` block that always prints `"done"` whether or not an error occurs.

## Navigation

Previous: [Chapter 5: Collections](../05_collections/README.md)  
Next: [Chapter 7: Iterations](../07_iterations/README.md)
