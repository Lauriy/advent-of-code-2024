from src.day_10 import solve_first
from src.day_10 import solve_second


def test_solve_first_example_1() -> None:
    assert solve_first("in/day_10_example_1.txt") == 2


def test_solve_first_example_2() -> None:
    assert solve_first("in/day_10_example_2.txt") == 4


def test_solve_first_example_3() -> None:
    assert solve_first("in/day_10_example_3.txt") == 3


def test_solve_first_example_4() -> None:
    assert solve_first("in/day_10_example_4.txt") == 36


def test_solve_first() -> None:
    assert solve_first("in/day_10.txt") == 472


def test_solve_second_example_4() -> None:
    assert solve_second("in/day_10_example_4.txt") == 81


def test_solve_second_example_5() -> None:
    assert solve_second("in/day_10_example_5.txt") == 3


def test_solve_second_example_6() -> None:
    assert solve_second("in/day_10_example_6.txt") == 13


def test_solve_second_example_7() -> None:
    assert solve_second("in/day_10_example_7.txt") == 227


def test_solve_second() -> None:
    assert solve_second("in/day_10.txt") == 969
