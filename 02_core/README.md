# Chapter 2: Core Types

Scalars, control flow, text, bytes, and the workhorse collections you will use every day.

## What You'll Learn

- `int`, `float`, `None`, and `bool`
- `if` / `while` / `for` control flow
- String literals, escapes, raw strings, and Unicode
- Bytes vs text, plus simple lists and dicts

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_int.py](./01_int.py) | Integer literals and arithmetic |
| [02_float.py](./02_float.py) | Floating-point values |
| [03_none.py](./03_none.py) | The `None` singleton |
| [04_bool.py](./04_bool.py) | Boolean values and truthiness |
| [05_rational.py](./05_rational.py) | Relational comparisons |
| [06_conditional.py](./06_conditional.py) | `if` / `elif` / `else` branching |
| [07_loops.py](./07_loops.py) | `while` loops, augmented assignment, `break` |
| [08_string.py](./08_string.py) | Basic `str` literals |
| [09_string_literals.py](./09_string_literals.py) | Adjacent literals, escapes, raw backslashes |
| [10_string_features.py](./10_string_features.py) | Raw paths and string helpers |
| [11_bytes.py](./11_bytes.py) | Bytes literals |
| [12_bytes_unicode.py](./12_bytes_unicode.py) | Encoding Unicode text to bytes |
| [13_list.py](./13_list.py) | Mutable list basics |
| [14_dict.py](./14_dict.py) | Mapping keys to values |
| [15_for_loop.py](./15_for_loop.py) | `for` over sequences |
| [16_sample.py](./16_sample.py) | Fetching and splitting words from a URL |

## Key Concepts

### Scalar Types

- `int` — arbitrary-precision integer
- `float` — 64-bit floating point
- `None` — the null object
- `bool` — `True` / `False`

### Control Flow

```python
if expression:
    block

while expression:
    block
```

- `break` exits a loop early; `07_loops.py` uses a non-interactive demo when stdin is not a TTY.

### Strings And Bytes

- `str` is an immutable sequence of Unicode code points.
- Escape sequences:

  ![Escape Sequences](../00_images/escape-sequences.PNG)

- Bytes literals use a `b` prefix; convert with `str.encode()` / `bytes.decode()`.

### Lists And Dicts

- Lists are mutable heterogeneous sequences (`append`, indexing).
- Dicts map keys to values: `{k1: v1, k2: v2}`.

## How To Run

```bash
python 02_core/01_int.py
python 02_core/07_loops.py
python 02_core/16_sample.py
```

## Try It Yourself

- Write a `while` loop that prints only multiples of 3 below 30.
- Encode a non-ASCII string to UTF-8 and decode it back.
- Build a small phone-book `dict` and look up a name that is missing (catch the `KeyError`).

## Navigation

Previous: [Chapter 1: Fundamentals](../01_fundamentals/README.md)  
Next: [Chapter 3: Modularity](../03_modularity/README.md)
