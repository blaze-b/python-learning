# Chapter 7: Iterations

Comprehensions, the iteration protocol, generators, and tools from `itertools`.

## What You'll Learn

- List and dict comprehensions (with filters)
- Iterable vs iterator and `StopIteration`
- Generator functions and generator expressions
- Bounding infinite streams with `islice`
- `any` / `all` / `zip` / `chain` patterns

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_comprehensions.py](./01_comprehensions.py) | List comprehensions over words |
| [02_dict_comprehensions.py](./02_dict_comprehensions.py) | Building and inverting mappings |
| [03_filtering_comprehensions.py](./03_filtering_comprehensions.py) | Filtering primes in a comprehension |
| [04_iteration_protocols.py](./04_iteration_protocols.py) | Manual `iter` / `next` usage |
| [05_generator.py](./05_generator.py) | A simple `yield`-based generator |
| [06_generator.py](./06_generator.py) | Composable generator pipelines (`take`) |
| [07_generator.py](./07_generator.py) | Infinite Lucas sequence (bounded for demos) |
| [08_generator_expressions.py](./08_generator_expressions.py) | Lazy generator expressions |
| [09_iterator_tools.py](./09_iterator_tools.py) | `itertools.islice` over primes |
| [10_iteration_tools_boolean_aggregation.py](./10_iteration_tools_boolean_aggregation.py) | `any` and `all` |
| [11_iteration_tools_zip.py](./11_iteration_tools_zip.py) | `zip`, `chain`, and bounded prime streaming |

## Key Concepts

### Comprehensions

```python
[expr(item) for item in iterable]
{key_expr(item): value_expr(item) for item in iterable}
```

- Prefer no side effects inside comprehension bodies.
- Use `dict.items()` when the source is already a mapping.

### Iteration Protocol

- **iterable** — passed to `iter()` to produce an iterator.
- **iterator** — passed to `next()`; ends with `StopIteration`.

### Generators

- `yield` builds lazy sequences; they can model infinite data.
- Always bound infinite generators when materializing (see `07_generator.py`).

### Iterator Tools

- Built-ins: `enumerate`, `sum`, `any`, `all`, `zip`.
- `itertools`: `islice`, `count`, `chain`.

## How To Run

```bash
python 07_iterations/01_comprehensions.py
python 07_iterations/07_generator.py
python 07_iterations/11_iteration_tools_zip.py
```

## Try It Yourself

- Write a dict comprehension that maps each word to its length.
- Implement `take(n, iterable)` yourself with `islice`.
- Stream the first 15 prime Lucas numbers without building a full list.

## Navigation

Previous: [Chapter 6: Exceptions](../06_exceptions/README.md)  
Next: [Chapter 8: Classes](../08_classes/README.md)
