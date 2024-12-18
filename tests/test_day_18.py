from src.day_18 import solve_first
from src.day_18 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_18_example.txt") == 22


def test_solve_first() -> None:
    result = solve_first("day_18.txt")
    assert result > 140
    assert result == 248


def test_solve_second_example() -> None:
    assert solve_second("day_18_example.txt") == "6,1"


def test_solve_second() -> None:
    result = solve_second("day_18.txt")
    assert result == "32,55"
