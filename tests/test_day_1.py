from src.day_1 import solve_first
from src.day_1 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_1_example.txt") == 11


def test_solve_first() -> None:
    result = solve_first("in/day_1.txt")
    assert result == 2166959


def test_solve_second_example() -> None:
    assert solve_second("in/day_1_example.txt") == 31


def test_solve_second() -> None:
    result = solve_second("in/day_1.txt")
    assert result == 23741109
