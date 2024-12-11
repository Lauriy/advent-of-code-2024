from src.day_11 import solve_first
from src.day_11 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_11_example.txt") == 55312


def test_solve_first() -> None:
    assert solve_first("in/day_11.txt") == 199753


def test_solve_second_example() -> None:
    assert solve_second("in/day_11_example.txt") == 65601038650482


def test_solve_second() -> None:
    assert solve_second("in/day_11.txt") == 239413123020116
