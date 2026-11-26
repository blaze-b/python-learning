# Chapter 5: Collections

Tuples, strings, ranges, lists, dictionaries, sets, and the protocols that tie them together.

## What You'll Learn

- Tuple packing/unpacking and string joining / f-strings
- `range` and `enumerate`
- List indexing, slicing, copy, insert, reverse, and sort
- Dict updates/iteration and set algebra
- Collection protocols (container, sized, iterable, sequence)

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_tuples.py](./01_tuples.py) | Tuple literals and unpacking |
| [02_strings.py](./02_strings.py) | Joining and formatting strings |
| [03_f_string.py](./03_f_string.py) | f-string interpolation (PEP 498) |
| [04_ranges.py](./04_ranges.py) | `range(start, stop, step)` |
| [05_enumerate.py](./05_enumerate.py) | Index/value pairs via `enumerate` |
| [06_lists.py](./06_lists.py) | Negative indices |
| [07_lists_slicing.py](./07_lists_slicing.py) | Slice notation |
| [08_lists_copy.py](./08_lists_copy.py) | Shallow copies of lists |
| [09_list_index.py](./09_list_index.py) | `index`, `count`, `in`, `remove`, `del` |
| [10_list_insert.py](./10_list_insert.py) | Inserting into a list |
| [11_list_reverse_sort.py](./11_list_reverse_sort.py) | In-place reverse and sort |
| [12_list_sort.py](./12_list_sort.py) | Sorting with a key callable |
| [13_dict.py](./13_dict.py) | Dict creation, update, and iteration |
| [14_dict_pp.py](./14_dict_pp.py) | Pretty-printing nested dicts |
| [15_sets.py](./15_sets.py) | Set literals and membership |
| [16_sets_algebra.py](./16_sets_algebra.py) | Union, intersection, difference |

## Key Concepts

### Built-In Collections

- **Tuples** — immutable sequences; unpacking destructures into names.
- **Strings** — prefer `str.join()` over repeated `+`; use f-strings for interpolation.
- **Range** — `range(stop)` / `range(start, stop)` / `range(start, stop, step)` (no keyword args).
- **Lists** — negative indices, slicing, `index` / `insert` / `reverse` / `sort`.
- **Dicts** — shallow copies; `update` merges; iterate with `items()` for pairs.

  ![Dict Overview](../00_images/dict.JPG)

- **Sets** — unordered unique hashable elements; support algebra operations.

### Protocols

![Collection Protocols](../00_images/protocols.JPG)

- Container: `in` / `not in`
- Sized: `len(container)`
- Iterable: yields items on demand
- Sequence: indexing, `index`, `count`, `reversed`

## How To Run

```bash
python 05_collections/01_tuples.py
python 05_collections/13_dict.py
python 05_collections/16_sets_algebra.py
```

## Try It Yourself

- Unpack a nested tuple of `(name, (lat, lon))`.
- Sort a list of words by length using `key=len`.
- Given two sets of names, print people who appear in exactly one set (symmetric difference).

## Navigation

Previous: [Chapter 4: Objects And Types](../04_objects_types/README.md)  
Next: [Chapter 6: Exceptions](../06_exceptions/README.md)
