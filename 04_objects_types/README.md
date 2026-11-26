# Chapter 4: Objects And Types

How Python binds names to objects: identity, mutability, argument passing, defaults, and scopes.

## What You'll Learn

- Object identity (`id`, `is`) versus value equality (`==`)
- Pass-by-object-reference and mutating arguments in place
- Why mutable default arguments are dangerous
- LEGB scoping and rebinding with `global`
- That functions and modules are first-class objects

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_id.py](./01_id.py) | `id()` of simple objects |
| [02_augmented_assignment.py](./02_augmented_assignment.py) | Augmented assignment on numbers |
| [03_mutable_objects.py](./03_mutable_objects.py) | Mutating a list through two names |
| [04_value_vs_identity.py](./04_value_vs_identity.py) | `==` vs `is` for lists |
| [05_argument_passing.py](./05_argument_passing.py) | Passing a list into a function |
| [06_replace_argument_value.py](./06_replace_argument_value.py) | Rebinding a parameter does not rebind the caller |
| [07_mutable_args.py](./07_mutable_args.py) | Mutating list contents via a parameter |
| [08_return_semantics.py](./08_return_semantics.py) | Returning a reference to a mutable object |
| [09_default_arguments.py](./09_default_arguments.py) | Keyword defaults for a banner printer |
| [10_default_values.py](./10_default_values.py) | Defaults evaluated at `def` time |
| [11_default_values_mutable.py](./11_default_values_mutable.py) | Shared mutable default trap |
| [12_default_values_use_immutable.py](./12_default_values_use_immutable.py) | Safe pattern: default `None`, then create a list |
| [13_python_type_systems.py](./13_python_type_systems.py) | Dynamic typing without implicit conversions |
| [14_scoping_global_rebinding.py](./14_scoping_global_rebinding.py) | Local shadowing vs `global` rebinding |
| [15_everything_is_an_object.py](./15_everything_is_an_object.py) | Treating a module as an object |
| [samples/word.py](./samples/word.py) | Sample module reused as an object |

## Key Concepts

### Value Vs Identity

- `==` compares values; `is` compares object identity.
- Two equal lists can still be distinct objects.

### Default Value Evaluation

- Default arguments are evaluated when `def` runs, once.
- Prefer **immutable** defaults; use `None` and create mutables inside the body.

### Scopes (LEGB)

- Local → Enclosing → Global → Built-in.
- Use `global` only when you must rebind a module-level name from inside a function.

## How To Run

```bash
python 04_objects_types/04_value_vs_identity.py
python 04_objects_types/11_default_values_mutable.py
python 04_objects_types/14_scoping_global_rebinding.py
```

## Try It Yourself

- Demonstrate that `a = []; b = a; b.append(1)` changes `a`.
- Fix a function that accidentally shares a default list across calls.
- Rewrite `14_scoping_global_rebinding.py` using a mutable counter object instead of `global`.

## Navigation

Previous: [Chapter 3: Modularity](../03_modularity/README.md)  
Next: [Chapter 5: Collections](../05_collections/README.md)
