# 04 — Objects and types

## Value vs identity equality

- Value equality (`==`) and identity equality (`is`) are different concepts
- Comparison by value can be controlled programmatically

## Default value evaluation

- `def` is a statement executed at runtime
- Default args are evaluated when `def` runs
- Prefer **immutable** default values; mutable defaults share state across calls

## Type systems

- Python will not generally perform implicit conversion between types

## Scopes (LEGB)

- Local → Enclosing → Global → Built-in
- Names can be rebound to objects of any type
- Use `global` when rebinding a module-level name from inside a function

## Everything is an object

- Functions, classes, and modules are first-class objects

## Scripts & samples

`01_id.py` … `15_everything_is_an_object.py`, plus `samples/word.py` (URL word fetch).
