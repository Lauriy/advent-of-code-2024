from src.day_22 import solve_first
from src.day_22 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_22_example_1.txt") == 37327623


def test_solve_first() -> None:
    assert solve_first("day_22.txt") == 19847565303


def test_solve_second_example() -> None:
    assert solve_second("day_22_example_2.txt") == 23


def test_solve_second() -> None:
    result = solve_second("day_22.txt")
    assert result > 2242
    assert result == 2050
