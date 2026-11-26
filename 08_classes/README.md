# 08 — Classes

- Classes define structure and behaviour; `__init__` initializes new instances
- Class invariants should hold for an object’s lifetime
- **Law of Demeter** — talk only to close collaborators
- **Tell, don’t ask** — tell objects what to do rather than probing state
- **Polymorphism / duck typing** — uniform interfaces across types
- **Inheritance** — mainly for sharing implementation; Python uses late binding

## Samples

| Module | Focus |
|--------|--------|
| `samples/air_travel_0.py` | `Flight` / `Aircraft` basics & validation |
| `samples/air_travel_1.py` | Seating, allocate / relocate, boarding cards |
| `samples/air_travel_2.py` | Inheritance (`AirbusA319`, `Boeing777`) |

## Scripts

`01_main.py` … `05_main.py` exercise the sample modules.
