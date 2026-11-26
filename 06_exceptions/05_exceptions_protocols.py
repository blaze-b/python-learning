z = [4, 1, 3]

# Will raise IndexError for out-of-bounds indexing
try:
    print(z[4])
except IndexError as e:
    print(f"IndexError: {e}")

# Will raise ValueError for invalid int conversion
try:
    print(int("jim"))
except ValueError as e:
    print(f"ValueError: {e}")

codes = dict(gb=44, us=1, no=47, fr=33, es=34)
# Will raise KeyError for a missing mapping key
try:
    print(codes["de"])
except KeyError as e:
    print(f"KeyError: {e}")
