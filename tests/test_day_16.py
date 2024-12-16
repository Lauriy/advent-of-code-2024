from src.day_16 import solve_first
from src.day_16 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_16_example.txt") == 7036


def test_solve_first() -> None:
    assert solve_first("day_16.txt") == 99488


def test_solve_second_example() -> None:
    assert solve_second("day_16_example.txt") == 45


def test_solve_second() -> None:
    assert solve_second("day_16.txt") == 516
