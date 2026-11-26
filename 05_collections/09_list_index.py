w = "the quick brown fox jumps over the lazy dog".split()

print(w)

index = w.index("fox")

print(index)

# index = w.index('unicorn')

print(index)

count = w.count("the")

print(count)

print(37 in [25, 26, 35, 37, 78, 78])

print(37 not in [25, 26, 35, 37, 78, 78])

# Del / remove — list.remove() mutates in place and returns None
w = "jackass love my big sphinx of quartz".split()

print(w)

w.remove("jackass")

print(w)

del w[w.index("quartz")]

print(w)
