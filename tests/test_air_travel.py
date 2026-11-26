"""Unit tests for the air_travel sample modules."""

from __future__ import annotations

import pytest


def test_flight_number_and_airline(air_travel_path):
    from samples.air_travel_0 import Flight

    flight = Flight("SN060")
    assert flight.number() == "SN060"
    assert flight.airline() == "SN"


@pytest.mark.parametrize(
    "number",
    ["060", "sm060", "SNabcd", "SN"],
)
def test_flight_rejects_invalid_numbers(air_travel_path, number):
    from samples.air_travel_0 import Flight

    with pytest.raises(ValueError):
        Flight(number)


def test_aircraft_seating_plan(air_travel_path):
    from samples.air_travel_0 import Aircraft

    aircraft = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
    rows, seats = aircraft.seating_plan()
    assert list(rows) == list(range(1, 23))
    assert seats == "ABCDEF"


def test_allocate_and_relocate(air_travel_path):
    from samples.air_travel_1 import Aircraft, Flight

    flight = Flight(
        "BA758",
        Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6),
    )
    flight.allocate_seat("12A", "Ada")
    with pytest.raises(ValueError, match="already occupied"):
        flight.allocate_seat("12A", "Grace")

    flight.relocate_seat("12A", "15D")
    assert flight._seating[12]["A"] is None
    assert flight._seating[15]["D"] == "Ada"


def test_num_available_seats(air_travel_path):
    from samples.air_travel_1 import Aircraft, Flight

    flight = Flight(
        "BA758",
        Aircraft("G-EUPT", "Airbus A319", num_rows=2, num_seats_per_row=2),
    )
    assert flight.num_available_seats() == 4
    flight.allocate_seat("1A", "Ada")
    assert flight.num_available_seats() == 3


def test_inheritance_models(air_travel_path):
    from samples.air_travel_2 import AirbusA319, Boeing777

    a319 = AirbusA319("G-EZBT")
    assert a319.model() == "Airbus A319"
    assert a319.num_seats() == 22 * 6

    b777 = Boeing777("N717AN")
    assert b777.model() == "Boeing 777"
    assert b777.num_seats() == 22 * 10
