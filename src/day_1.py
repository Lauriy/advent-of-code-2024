def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)

    return left_list, right_list


def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = 0
    for left, right in zip(left_sorted, right_sorted, strict=False):
        distance = abs(left - right)
        total_distance += distance

    return total_distance


def calculate_similarity_score(left_list, right_list):
    right_counts = {}
    for num in right_list:
        right_counts[num] = right_counts.get(num, 0) + 1

    total_score = 0
    for num in left_list:
        count = right_counts.get(num, 0)
        total_score += num * count

    return total_score


def solve_first(file_name: str) -> int:
    return calculate_total_distance(*read_input(file_name))


def solve_second(file_name: str) -> int:
    return calculate_similarity_score(*read_input(file_name))
