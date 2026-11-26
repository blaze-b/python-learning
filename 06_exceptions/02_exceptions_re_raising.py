from samples.exception_2 import string_log

# Demonstrates that convert() re-raises KeyError after logging.
try:
    string_log("Ouch!".split())
except KeyError as e:
    print(f"Re-raised as expected: {e!r}")
