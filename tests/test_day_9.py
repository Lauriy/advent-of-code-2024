from src.day_9 import solve_first
from src.day_9 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_9_example.txt") == 1928


def test_solve_first() -> None:
    result = solve_first("in/day_9.txt")
    assert result == 6283170117911


def test_solve_second_example() -> None:
    assert solve_second("in/day_9_example.txt") == 2858


def test_solve_second() -> None:
    result = solve_second("in/day_9.txt")
    assert result == 6307653242596
