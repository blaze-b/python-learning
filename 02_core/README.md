# 02 — Core language

## Scalar types

- `int` — arbitrary-precision integer
- `float` — 64-bit floating-point numbers
- `None` — the null object
- `bool` (`True`, `False`) — boolean logical values

## Relational operators

- Used for value-equality checks

## Conditional statements

Branch execution based on the value of an expression:

```python
if expression:
    block
```

## Loops

```python
while expression:
    block
```

- `break` is supported
- The interactive loop demo in `07_loops.py` uses a non-interactive fallback when stdin is not a TTY

## Strings

- Datatype: `str`
- Sequence of Unicode code points
- Immutable
- Supports single- and multi-line literals (`''`, `""`)
- Concatenation of adjacent literals
- Universal newlines
- Raw strings
- Use the `str` constructor to convert other types
- Access individual characters with square-bracket indexing
- Rich API; can contain Unicode

### String literals

- Multiline strings or escape sequences for newlines
- List of escape sequences:

  ![Escape sequences](../00_images/escape-sequences.PNG)

## Bytes

- Datatype for sequences of bytes / raw binary data
- Literals prefixed with `b`
- Use `str.encode()` and `bytes.decode()` for conversion

## Lists

- Mutable, heterogeneous sequences delimited by `[]`
- Grow with `append()`; use `list()` to build from other sequences

## Dict

- Map keys to values; literals use curly braces

```python
{k1: v1, k2: v2}
```

## for-loop

```python
for item in iterable:
    ...
```

## Scripts

`01_int.py` through `16_sample.py` cover scalars, control flow, strings, bytes, lists, and dicts.
