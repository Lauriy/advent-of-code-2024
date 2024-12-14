from src.day_14 import solve_first
from src.day_14 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_14_example.txt") == 12


def test_solve_first() -> None:
    result = solve_first("in/day_14.txt")
    assert result == 220971520


def test_solve_second() -> None:
    result = solve_second("in/day_14.txt")
    assert result > 6354  # Known wrong answers
    assert result < 10402
    assert result < 27160
    assert result == 6355  # Off-by-one
