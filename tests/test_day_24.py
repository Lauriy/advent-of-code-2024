from src.day_24 import solve_first
from src.day_24 import solve_second


def test_solve_first_example_1() -> None:
    assert solve_first("day_24_example_1.txt") == 4


def test_solve_first_example_2() -> None:
    assert solve_first("day_24_example_2.txt") == 2024


def test_solve_first() -> None:
    assert solve_first("day_24.txt") == 65635066541798


def test_solve_second() -> None:
    assert len(solve_second("day_24.txt").split(",")) == 8
