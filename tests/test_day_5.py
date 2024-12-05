from src.day_5 import solve_first, solve_second


def test_solve_first_example():
    assert solve_first('in/day_5_example.txt') == 143


def test_solve_first():
    result = solve_first('in/day_5.txt')
    print(f"Day 5, part 1: {result}")
    assert result == 4872


def test_solve_second_example():
    assert solve_second('in/day_5_example.txt') == 123


def test_solve_second():
    result = solve_second('in/day_5.txt')
    print(f"Day 5, part 2: {result}")
    assert result == 5564
    