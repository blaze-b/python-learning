# 05 — Collections

## Built-in collections

### Tuples

- Immutable sequences of arbitrary objects
- Tuple unpacking destructures into named references

### Strings

- Prefer `str.join()` over repeated `+` (avoids temporaries)
- **PEP 498** f-strings embed expressions in literals

### Range

- `range(stop)` / `range(start, stop)` / `range(start, stop, step)`
- Does not support keyword arguments

### Enumerate

- Builds an iterable of `(index, value)` tuples

### Lists

- Negative indices; slicing `a_list[start:stop]`
- `list.index()`, `del`, `insert()`, `reverse()`, `sort()`

### Dict

![Dict overview](../00_images/dict.JPG)

- Shallow copies; `dict.update()` merges entries
- Iterate keys by default; use `dict.items()` for pairs

### Set

- Unordered collection of unique, hashable elements

## Protocols

![Collection protocols](../00_images/protocols.JPG)

- Container: `in` / `not in`
- Sized: `len(container)`
- Iterable: yields items on demand
- Sequence: indexing, `index`, `count`, `reversed`

## Scripts

`01_tuples.py` … `16_sets_algebra.py`
