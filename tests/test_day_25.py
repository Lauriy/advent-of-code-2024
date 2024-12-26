from src.day_25 import solve_first
from src.day_25 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_25_example.txt") == 3


def test_solve_first() -> None:
    assert solve_first("day_25.txt") == 3395


def test_solve_second() -> None:
    assert solve_second("day_25.txt") == "Not implemented"
