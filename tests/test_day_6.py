from src.day_6 import solve_first, solve_second


def test_solve_first_example():
    assert solve_first('in/day_6_example.txt') == 41


def test_solve_first():
    result = solve_first('in/day_6.txt')
    print(f"\nDay 6, part 1 solution: {result}")
    assert result == 5269


def test_solve_second_example():
    assert solve_second('in/day_6_example.txt') == 6


def test_solve_second():
    result = solve_second('in/day_6.txt')
    print(f"\nDay 6, part 2 solution: {result}")
    
    wrong_answers = {119, 365, 395, 399, 807, 1024, 2041, 2287, 15811}
    assert result not in wrong_answers, f"Got known wrong answer: {result}"
    assert result == 1957
