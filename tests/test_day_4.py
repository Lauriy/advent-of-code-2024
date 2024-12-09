from src.day_4 import solve_first
from src.day_4 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_4_example.txt") == 18


def test_solve_first() -> None:
    result = solve_first("in/day_4.txt")
    assert result == 2599


def test_solve_second_example() -> None:
    assert solve_second("in/day_4_example.txt") == 9


def test_solve_second() -> None:
    result = solve_second("in/day_4.txt")
    assert result == 1948
