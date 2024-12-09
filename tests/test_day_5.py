from src.day_5 import solve_first
from src.day_5 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_5_example.txt") == 143


def test_solve_first() -> None:
    result = solve_first("in/day_5.txt")
    assert result == 4872


def test_solve_second_example() -> None:
    assert solve_second("in/day_5_example.txt") == 123


def test_solve_second() -> None:
    result = solve_second("in/day_5.txt")
    assert result == 5564
