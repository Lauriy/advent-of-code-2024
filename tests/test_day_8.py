from src.day_8 import solve_first
from src.day_8 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_8_example.txt") == 14


def test_solve_first() -> None:
    result = solve_first("in/day_8.txt")
    assert result == 381


def test_solve_second_example() -> None:
    assert solve_second("in/day_8_example.txt") == 34


def test_solve_second() -> None:
    result = solve_second("in/day_8.txt")
    assert result == 1184
