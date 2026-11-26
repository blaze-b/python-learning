import sys

c = 5

while c != 0:
    print(c)
    c -= 1

# Augmented assignment
print(c)
c += 10
print(10)
c -= 10
print(c)
c *= 10
print(c)

# Break statement — interactive when stdin is a TTY; otherwise use a demo value.
while True:
    if sys.stdin.isatty():
        print("Input the number....")
        response = input()
    else:
        response = "14"
        print(f"Input the number.... (non-interactive demo: {response})")
    if int(response) % 7 == 0:
        break
