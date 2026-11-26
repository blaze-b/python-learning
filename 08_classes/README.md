# Chapter 8: Classes

Object-oriented modelling with a small airline domain: flights, aircraft, and seating.

## What You'll Learn

- Defining classes with `__init__` and instance methods
- Validating construction arguments
- Encapsulating seating plans and passenger allocation
- Inheritance for shared behaviour across aircraft models
- Polymorphism via duck typing (boarding-card printers)

## Lessons

| Script | What It Shows |
|--------|---------------|
| [01_main.py](./01_main.py) | Creating a `Flight` and rejecting invalid numbers |
| [02_main.py](./02_main.py) | Constructing an `Aircraft` seating plan |
| [03_main.py](./03_main.py) | Allocating seats on a flight |
| [04_main.py](./04_main.py) | Relocating passengers and printing boarding cards |
| [05_main.py](./05_main.py) | Subclassed aircraft (`AirbusA319`, `Boeing777`) |
| [samples/air_travel_0.py](./samples/air_travel_0.py) | Basic `Flight` / `Aircraft` with route validation |
| [samples/air_travel_1.py](./samples/air_travel_1.py) | Seating map, allocate / relocate, boarding cards |
| [samples/air_travel_2.py](./samples/air_travel_2.py) | Inheritance hierarchy for concrete models |

## Key Concepts

- Classes control initial state, attributes, and methods; `__init__` initializes new instances.
- Keep **class invariants** true for the lifetime of an object (e.g. valid flight numbers).
- **Law of Demeter** — talk mainly to close collaborators.
- **Tell, Don’t Ask** — tell objects what to do instead of probing their state.
- **Duck typing** — if it provides the needed methods, it can fill the role.
- Inheritance shares implementation; Python resolves methods with late binding.

## How To Run

```bash
python 08_classes/01_main.py
python 08_classes/04_main.py
python 08_classes/05_main.py
```

## Try It Yourself

- Add a method that returns passengers sorted by seat letter.
- Raise a clear error when relocating into an occupied seat (already done — write a test for it).
- Introduce a third aircraft subclass with its own seating plan.

## Navigation

Previous: [Chapter 7: Iterations](../07_iterations/README.md)  
Next: [Chapter 9: Files And I/O](../09_io_file/README.md)
