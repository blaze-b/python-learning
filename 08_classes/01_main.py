from samples.air_travel_0 import Flight

flight = Flight("SN060")

print(type(flight))

print(flight.number())

# Not recommended — accessing the "private" attribute directly
print(flight._number)

for invalid in ("060", "sm060", "snanbe"):
    try:
        Flight(invalid)
    except ValueError as e:
        print(f"Rejected {invalid!r}: {e}")
