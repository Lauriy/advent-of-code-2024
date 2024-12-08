from src.day_8 import solve_first, solve_second


def test_solve_first_example():
    assert solve_first('in/day_8_example.txt') == 14


def test_solve_first():
    result = solve_first('in/day_8.txt')
    assert result == 381
    print(f"\nDay 8, part 1 solution: {result}")


def test_solve_second_example():
    assert solve_second('in/day_8_example.txt') == 34


def test_solve_second():
    result = solve_second('in/day_8.txt')
    assert result == 1184
    print(f"\nDay 8, part 2 solution: {result}")
