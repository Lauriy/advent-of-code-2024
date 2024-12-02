def is_safe_report(levels):
    # Check if all adjacent differences are between 1 and 3
    diffs = []
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        diffs.append(diff)
    
    # Check if all differences are in the same direction (all positive or all negative)
    return all(d > 0 for d in diffs) or all(d < 0 for d in diffs)

def is_safe_with_dampener(levels):
    # First check if it's safe without dampener
    if is_safe_report(levels):
        return True
    
    # Try removing each level one at a time
    for i in range(len(levels)):
        dampened_levels = levels[:i] + levels[i+1:]
        if is_safe_report(dampened_levels):
            return True
    
    return False

def solve_first(file_name: str) -> int:
    safe_count = 0
    with open(file_name) as f:
        for line in f:
            levels = [int(x) for x in line.strip().split()]
            if is_safe_report(levels):
                safe_count += 1

    return safe_count

def solve_second(file_name: str) -> int:
    safe_count = 0
    with open(file_name) as f:
        for line in f:
            levels = [int(x) for x in line.strip().split()]
            if is_safe_with_dampener(levels):
                safe_count += 1
                
    return safe_count
