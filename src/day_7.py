from itertools import product


def parse_input(filename: str) -> list[tuple[int, list[int]]]:
    with open(filename) as f:
        input_text = f.read()
    equations = []
    for line in input_text.strip().splitlines():
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = [int(x) for x in numbers.split()]
        equations.append((test_value, numbers))

    return equations


def evaluate_expression(numbers: list[int], operators: list[str]) -> int:
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == "+":
            result += numbers[i + 1]
        elif op == "*":
            result *= numbers[i + 1]
        else:  # op == '||'
            result = int(str(result) + str(numbers[i + 1]))

    return result


def can_make_test_value(
    test_value: int,
    numbers: list[int],
    use_concat: bool = False,
) -> bool:
    operators = ["+", "*"] if not use_concat else ["+", "*", "||"]
    num_operators = len(numbers) - 1

    for ops in product(operators, repeat=num_operators):
        if evaluate_expression(numbers, ops) == test_value:
            return True

    return False


def solve_first(filename: str) -> int:
    equations = parse_input(filename)
    total = 0

    for test_value, numbers in equations:
        if can_make_test_value(test_value, numbers):
            total += test_value

    return total


def solve_second(filename: str) -> int:
    equations = parse_input(filename)
    total = 0

    for test_value, numbers in equations:
        if can_make_test_value(test_value, numbers, use_concat=True):
            total += test_value

    return total
