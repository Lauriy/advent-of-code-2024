from src.day_4 import solve_first, solve_second

def test_solve_first_example():
    assert solve_first("in/day_4_example.txt") == 18

def test_solve_first():
    result = solve_first("in/day_4.txt")
    print("\nDay 4, part 1 solution:", result)
    assert result == 2599

def test_solve_second_example():
    assert solve_second("in/day_4_example.txt") == 9

def test_solve_second():
    result = solve_second("in/day_4.txt")
    print("\nDay 4, part 2 solution:", result)
    assert result == 1948
