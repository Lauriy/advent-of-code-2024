import functools
from pathlib import Path


def parse_input(input_text: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    rules_text, updates_text = input_text.strip().split("\n\n")

    rules: dict[int, set[int]] = {}
    for line in rules_text.splitlines():
        if not line:
            continue
        before, after = map(int, line.split("|"))
        if before not in rules:
            rules[before] = set()
        rules[before].add(after)

    updates = []
    for line in updates_text.splitlines():
        if line:
            update = list(map(int, line.split(",")))
            updates.append(update)

    return rules, updates


def is_valid_order(update: list[int], rules: dict[int, set[int]]) -> bool:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            page_before = update[i]
            page_after = update[j]

            if page_after in rules and page_before in rules[page_after]:
                return False

    return True


def get_middle_number(update: list[int]) -> int:
    return update[len(update) // 2]


def sort_by_rules(update: list[int], rules: dict[int, set[int]]) -> list[int]:
    def compare_pages(a: int, b: int) -> bool:
        if b in rules and a in rules[b]:
            return False  # a must come after b
        if a in rules and b in rules[a]:
            return True  # a must come before b

        return a < b  # default

    return sorted(
        update,
        key=functools.cmp_to_key(lambda a, b: -1 if compare_pages(a, b) else 1),
    )


def solve_first(input_path: str) -> int:
    input_text = Path(input_path).read_text()
    rules, updates = parse_input(input_text)

    total = 0
    for update in updates:
        if is_valid_order(update, rules):
            total += get_middle_number(update)

    return total


def solve_second(input_path: str) -> int:
    input_text = Path(input_path).read_text()
    rules, updates = parse_input(input_text)

    total = 0
    for update in updates:
        if not is_valid_order(update, rules):
            sorted_update = sort_by_rules(update, rules)
            total += get_middle_number(sorted_update)

    return total
