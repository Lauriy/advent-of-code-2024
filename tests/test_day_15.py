from src.day_15 import solve_first
from src.day_15 import solve_second


def test_solve_first_example_1() -> None:
    assert solve_first("day_15_example_1.txt") == 2028


def test_solve_first_example_2() -> None:
    assert solve_first("day_15_example_2.txt") == 10092


def test_solve_first() -> None:
    result = solve_first("day_15.txt")
    assert result < 1497492
    assert result == 1436690


def test_solve_second_example_1() -> None:
    assert solve_second("day_15_example_2.txt") == 9021


def test_solve_second() -> None:
    result = solve_second("day_15.txt")
    assert result == 1482350
