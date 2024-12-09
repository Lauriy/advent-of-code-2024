from src.day_7 import solve_first
from src.day_7 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_7_example.txt") == 3749


def test_solve_first() -> None:
    result = solve_first("in/day_7.txt")
    assert result == 538191549061


def test_solve_second_example() -> None:
    assert solve_second("in/day_7_example.txt") == 11387


def test_solve_second() -> None:
    result = solve_second("in/day_7.txt")
    assert result == 34612812972206
