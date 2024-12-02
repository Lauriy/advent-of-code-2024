from src.day_1 import solve_first, solve_second

def test_solve_first_example():
    assert solve_first("in/day_1_example.txt") == 11

def test_solve_first():
    result = solve_first("in/day_1.txt")
    print("\nDay 1, part 1 solution:", result)
    assert result == 2166959

def test_solve_second_example():
    assert solve_second("in/day_1_example.txt") == 31

def test_solve_second():
    result = solve_second("in/day_1.txt")
    print("\nDay 1, part 2 solution:", result)
    assert result == 23741109
