from collections import deque
from pathlib import Path


def read_input(filename: str) -> list[tuple[int, int]]:
    path = Path(__file__).parent.parent / "in" / filename

    return [tuple(map(int, line.split(","))) for line in path.read_text().splitlines()]


def get_grid_config(filename: str) -> tuple[int, tuple[int, int], int]:
    is_example = filename == "day_18_example.txt"

    return (
        7 if is_example else 71,
        (6, 6) if is_example else (70, 70),
        12 if is_example else 1024,
    )


def find_path(
    start: tuple[int, int],
    target: tuple[int, int],
    bytes_fallen: set[tuple[int, int]],
    grid_size: int,
    count_steps: bool = True,
) -> tuple[bool, int | None]:
    queue = deque([(0, start)] if count_steps else [start])
    seen = {start}

    while queue:
        steps, (x, y) = queue.popleft() if count_steps else (None, queue.popleft())

        if (x, y) == target or (
            target in bytes_fallen and abs(x - target[0]) + abs(y - target[1]) == 1
        ):
            return True, steps

        # down, right, up, left
        for direction_y, direction_x in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            next_position_x = x + direction_x
            next_position_y = y + direction_y
            next_position = (next_position_x, next_position_y)

            if (
                0 <= next_position_x < grid_size
                and 0 <= next_position_y < grid_size
                and next_position not in seen
                and next_position not in bytes_fallen
            ):
                seen.add(next_position)
                queue.append(
                    (steps + 1, next_position) if count_steps else next_position,
                )

    return False, None


def solve_first(filename: str) -> int:
    bytes_falling = read_input(filename)
    grid_size, target, max_bytes = get_grid_config(filename)
    bytes_fallen = set(bytes_falling[:max_bytes])

    found_path, steps = find_path((0, 0), target, bytes_fallen, grid_size)

    return steps if found_path else -1


def solve_second(filename: str) -> str:
    bytes_falling = read_input(filename)
    grid_size, target, _ = get_grid_config(filename)
    start = (0, 0)
    bytes_fallen = set()

    for x, y in bytes_falling:
        bytes_fallen.add((x, y))

        if (x, y) in {start, target} or not find_path(
            start,
            target,
            bytes_fallen,
            grid_size,
            count_steps=False,
        )[0]:
            return f"{x},{y}"

    return "No blocking byte found"
