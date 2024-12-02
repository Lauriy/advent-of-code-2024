from src.day_2 import solve_first, solve_second, is_safe_report, is_safe_with_dampener

def test_is_safe_report():
    assert is_safe_report([7, 6, 4, 2, 1]) == True  # Safe: decreasing by 1 or 2
    assert is_safe_report([1, 2, 7, 8, 9]) == False  # Unsafe: increase of 5
    assert is_safe_report([9, 7, 6, 2, 1]) == False  # Unsafe: decrease of 4
    assert is_safe_report([1, 3, 2, 4, 5]) == False  # Unsafe: mixed directions
    assert is_safe_report([8, 6, 4, 4, 1]) == False  # Unsafe: no change
    assert is_safe_report([1, 3, 6, 7, 9]) == True  # Safe: increasing by 1-3

def test_is_safe_with_dampener():
    assert is_safe_with_dampener([7, 6, 4, 2, 1]) == True   # Safe without removing any level
    assert is_safe_with_dampener([1, 2, 7, 8, 9]) == False  # Unsafe regardless
    assert is_safe_with_dampener([9, 7, 6, 2, 1]) == False  # Unsafe regardless
    assert is_safe_with_dampener([1, 3, 2, 4, 5]) == True   # Safe by removing 3
    assert is_safe_with_dampener([8, 6, 4, 4, 1]) == True   # Safe by removing middle 4
    assert is_safe_with_dampener([1, 3, 6, 7, 9]) == True   # Safe without removing any level

def test_solve_first_example():
    assert solve_first("in/day_2_example.txt") == 2

def test_solve_first():
    result = solve_first("in/day_2.txt")
    print("\nDay 2, part 1 solution:", result)
    assert result == 411

def test_solve_second_example():
    assert solve_second("in/day_2_example.txt") == 4

def test_solve_second():
    result = solve_second("in/day_2.txt")
    print("\nDay 2, part 2 solution:", result)
    assert result == 465
