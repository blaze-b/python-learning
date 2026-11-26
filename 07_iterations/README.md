# 07 — Iterations and iterables

## Comprehensions

```python
[expr(item) for item in iterable]
```

Dict form:

```python
{key_expr(item): value_expr(item) for item in iterable}
```

- Use `dict.items()` when the source is a mapping
- Prefer no side effects inside comprehensions

## Iteration protocol

- **iterable** — passed to `iter()` to produce an iterator
- **iterator** — passed to `next()`; ends with `StopIteration`

## Generators

- Lazy sequences defined with `yield`
- Can model infinite / very large sequences
- Always bound infinite generators when materializing (see `07_generator.py`)

## Iterator tools

- `enumerate()`, `sum()`, `any()`, `all()`, `zip()`
- `itertools.islice()`, `itertools.count()`, `itertools.chain()`

## Scripts

`01_comprehensions.py` … `11_iteration_tools_zip.py`
