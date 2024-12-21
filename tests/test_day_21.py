from src.day_21 import solve_first
from src.day_21 import solve_second


def test_first_example() -> None:
    assert solve_first("day_21_example.txt") == 126384


def test_solve_first() -> None:
    assert solve_first("day_21.txt") == 188398


def test_solve_second() -> None:
    assert solve_second("day_21.txt") == 230049027535970
