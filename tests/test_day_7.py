from src.day_7 import solve_first, solve_second


def test_solve_first_example():
    assert solve_first('in/day_7_example.txt') == 3749


def test_solve_first():
    result = solve_first('in/day_7.txt')
    print(f"\nDay 7, part 1 solution: {result}")
    assert result == 538191549061


def test_solve_second_example():
    assert solve_second('in/day_7_example.txt') == 11387


def test_solve_second():
    result = solve_second('in/day_7.txt')
    print(f"\nDay 7, part 2 solution: {result}")
    assert result == 34612812972206
