from collections import Counter
from pathlib import Path


def parse_input(input_text: str) -> list[int]:
    return [int(x) for x in input_text.strip().split()]


def transform_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])

        return [left, right]

    return [stone * 2024]


def blink_counter(stones: Counter[int]) -> Counter[int]:
    new_stones = Counter()

    for stone, count in stones.items():
        for new_stone in transform_stone(stone):
            new_stones[new_stone] += count

    return new_stones


def solve_first(input_path: str) -> int:
    stones = parse_input(Path(input_path).read_text())
    stone_counts = Counter(stones)

    for _ in range(25):
        stone_counts = blink_counter(stone_counts)

    return sum(stone_counts.values())


def solve_second(input_path: str) -> int:
    stones = parse_input(Path(input_path).read_text())
    stone_counts = Counter(stones)

    for _i in range(75):
        stone_counts = blink_counter(stone_counts)

    return sum(stone_counts.values())
