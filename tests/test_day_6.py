from src.day_6 import solve_first
from src.day_6 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("in/day_6_example.txt") == 41


def test_solve_first() -> None:
    result = solve_first("in/day_6.txt")
    assert result == 5269


def test_solve_second_example() -> None:
    assert solve_second("in/day_6_example.txt") == 6


def test_solve_second() -> None:
    result = solve_second("in/day_6.txt")

    wrong_answers = {119, 365, 395, 399, 807, 1024, 2041, 2287, 15811}
    assert result not in wrong_answers, f"Got known wrong answer: {result}"
    assert result == 1957
