from src.day_2 import is_safe_report
from src.day_2 import is_safe_with_dampener
from src.day_2 import solve_first
from src.day_2 import solve_second


def test_is_safe_report() -> None:
    assert is_safe_report([7, 6, 4, 2, 1]) is True  # Safe: decreasing by 1 or 2
    assert is_safe_report([1, 2, 7, 8, 9]) is False  # Unsafe: increase of 5
    assert is_safe_report([9, 7, 6, 2, 1]) is False  # Unsafe: decrease of 4
    assert is_safe_report([1, 3, 2, 4, 5]) is False  # Unsafe: mixed directions
    assert is_safe_report([8, 6, 4, 4, 1]) is False  # Unsafe: no change
    assert is_safe_report([1, 3, 6, 7, 9]) is True  # Safe: increasing by 1-3


def test_is_safe_with_dampener() -> None:
    assert (
        is_safe_with_dampener([7, 6, 4, 2, 1]) is True
    )  # Safe without removing any level
    assert is_safe_with_dampener([1, 2, 7, 8, 9]) is False  # Unsafe regardless
    assert is_safe_with_dampener([9, 7, 6, 2, 1]) is False  # Unsafe regardless
    assert is_safe_with_dampener([1, 3, 2, 4, 5]) is True  # Safe by removing 3
    assert is_safe_with_dampener([8, 6, 4, 4, 1]) is True  # Safe by removing middle 4
    assert (
        is_safe_with_dampener([1, 3, 6, 7, 9]) is True
    )  # Safe without removing any level


def test_solve_first_example() -> None:
    assert solve_first("in/day_2_example.txt") == 2


def test_solve_first() -> None:
    result = solve_first("in/day_2.txt")
    assert result == 411


def test_solve_second_example() -> None:
    assert solve_second("in/day_2_example.txt") == 4


def test_solve_second() -> None:
    result = solve_second("in/day_2.txt")
    assert result == 465
