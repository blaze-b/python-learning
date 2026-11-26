"""Demonstrate raiding a refrigerator."""

from contextlib import closing


class RefrigeratorRaider:
    """Raid a refrigerator"""

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == "deep fried pizza":
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("Close fridge door.")


def raid(food):
    r = RefrigeratorRaider()
    r.open()
    try:
        r.take(food)
    finally:
        r.close()


def raid_with_closing(food):
    with closing(RefrigeratorRaider()) as r:
        r.open()
        r.take(food)


def demo():
    raid("bacon")
    try:
        raid("deep fried pizza")
    except RuntimeError as e:
        print(f"Caught: {e}")

    raid_with_closing("bacon")
    try:
        raid_with_closing("deep fried pizza")
    except RuntimeError as e:
        print(f"Caught with closing(): {e}")


if __name__ == "__main__":
    demo()
