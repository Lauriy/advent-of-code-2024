from src.day_17 import solve_first
from src.day_17 import solve_second


def test_solve_first_example() -> None:
    assert solve_first("day_17_example_1.txt") == "4,6,3,5,6,3,5,2,1,0"


def test_solve_first() -> None:
    assert solve_first("day_17.txt") == "5,0,3,5,7,6,1,5,4"


def test_solve_second_example() -> None:
    assert solve_second("day_17_example_2.txt") == 117440  # 0o345300, very close


def test_solve_second() -> None:
    result = solve_second("day_17.txt")
    # known wrong answers
    assert result != 709160982436544
    assert result != 261209348580896

    assert result > 130604674290448
    assert result < 1044837394323584

    assert result == 164516454365621
