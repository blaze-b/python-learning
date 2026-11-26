from itertools import islice


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


# Infinite generators must be bounded when materializing a list.
print(list(islice(lucas(), 20)))
