from src.day_20 import solve_first
from src.day_20 import solve_second


def test_solve_first_example() -> None:
    assert (
        solve_first("day_20_example.txt") == 1
    )  # only one cheat saves >= 64 picoseconds


def test_solve_first() -> None:
    assert solve_first("day_20.txt") == 1521


def test_solve_second_example() -> None:
    assert (
        solve_second("day_20_example.txt") == 285
    )  # sum of all cheats that save >= 50 picoseconds


def test_solve_second() -> None:
    assert solve_second("day_20.txt") == 1013106
