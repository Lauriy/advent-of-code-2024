from src.day_19 import solve_first
from src.day_19 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_19_example.txt") == 6


def test_solve_first() -> None:
    assert solve_first("day_19.txt") == 296


def test_solve_second_example() -> None:
    assert solve_second("day_19_example.txt") == 16


def test_solve_second() -> None:
    assert solve_second("day_19.txt") == 619970556776002
