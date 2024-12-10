from collections import deque
from pathlib import Path

HEIGHT_TO_REACH = 9


def parse_input(input_text: str) -> list[list[int]]:
    grid = []
    for line in input_text.splitlines():
        if not line.strip():
            continue
        row = []
        for c in line:
            if c == ".":
                row.append(-1)  # impassable
            else:
                row.append(int(c))
        grid.append(row)

    return grid


def get_neighbors(x: int, y: int, grid: list[list[int]]) -> list[tuple[int, int]]:
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # right, left, down, up
        new_x, new_y = x + dx, y + dy
        if (
            0 <= new_x < len(grid)
            and 0 <= new_y < len(grid[0])
            and grid[new_x][new_y] != -1
        ):
            neighbors.append((new_x, new_y))

    return neighbors


def find_hiking_trails(
    start: tuple[int, int],
    grid: list[list[int]],
) -> set[tuple[int, int]]:
    reachable_nines = set()
    visited = set()
    queue = deque([(start, {start})])  # (current_pos, path)

    while queue:
        (x, y), path = queue.popleft()
        current_height = grid[x][y]

        if current_height == HEIGHT_TO_REACH:
            reachable_nines.add((x, y))
            continue

        for next_x, next_y in get_neighbors(x, y, grid):
            next_pos = (next_x, next_y)
            next_height = grid[next_x][next_y]

            if (
                next_height == current_height + 1
                and next_pos not in path
                and next_pos not in visited
            ):
                visited.add(next_pos)
                new_path = path | {next_pos}
                queue.append((next_pos, new_path))

    return reachable_nines


def find_trailheads(grid: list[list[int]]) -> list[tuple[int, int]]:
    trailheads = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                trailheads.append((i, j))

    return trailheads


def find_all_hiking_trails(start: tuple[int, int], grid: list[list[int]]) -> int:
    paths = 0
    visited_paths = set()
    queue = deque([(start, (start,))])

    while queue:
        (x, y), path = queue.popleft()
        current_height = grid[x][y]

        if current_height == HEIGHT_TO_REACH:
            path_key = tuple(sorted(path))  # unique
            if path_key not in visited_paths:
                paths += 1
                visited_paths.add(path_key)
            continue

        for next_x, next_y in get_neighbors(x, y, grid):
            next_pos = (next_x, next_y)
            next_height = grid[next_x][next_y]

            if next_height == current_height + 1 and next_pos not in path:
                new_path = (*path, next_pos)
                queue.append((next_pos, new_path))

    return paths


def solve_first(input_path: str) -> int:
    grid = parse_input(Path(input_path).read_text())
    trailheads = find_trailheads(grid)

    total_score = 0
    for start in trailheads:
        reachable_nines = find_hiking_trails(start, grid)
        total_score += len(reachable_nines)

    return total_score


def solve_second(input_path: str) -> int:
    grid = parse_input(Path(input_path).read_text())
    trailheads = find_trailheads(grid)

    total_rating = 0
    for start in trailheads:
        rating = find_all_hiking_trails(start, grid)
        total_rating += rating

    return total_rating
