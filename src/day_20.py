from collections import deque
from collections.abc import Iterator
from itertools import combinations
from pathlib import Path

type Coord = tuple[int, int]
type Grid = dict[Coord, str]
type Distance = dict[Coord, int]

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up


def read_grid(input_path: str | Path) -> Grid:
    input_path = Path("in") / input_path

    return {
        (x, y): char
        for y, row in enumerate(input_path.read_text().splitlines())
        for x, char in enumerate(row)
        if char != "#"
    }


def find_all_distances(grid: Grid, start_position: Coord) -> Distance:
    distances = {start_position: 0}
    positions_to_visit = deque([start_position])

    while positions_to_visit:
        current_position = positions_to_visit.popleft()
        current_x, current_y = current_position

        for direction_x, direction_y in DIRECTIONS:
            neighbor_position = (current_x + direction_x, current_y + direction_y)
            if neighbor_position in grid and neighbor_position not in distances:
                distances[neighbor_position] = distances[current_position] + 1
                positions_to_visit.append(neighbor_position)

    return distances


def find_valid_shortcuts(
    distances: Distance,
    max_length: int,
    min_savings: int,
) -> Iterator[tuple[Coord, Coord, int]]:
    # https://www.reddit.com/r/adventofcode/comments/1hicdtb/comment/m2y56t8/
    for (start_pos, start_dist), (end_pos, end_dist) in combinations(
        distances.items(),
        2,
    ):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        # Manhattan
        direct_distance = abs(end_x - start_x) + abs(end_y - start_y)
        if direct_distance > max_length:
            # Not useful
            continue

        # Calculate time saved by taking the shortcut:
        # end_dist = steps from Start to End normally
        # start_dist = steps from Start to shortcut entrance
        # direct_distance = length of the shortcut
        # If end_dist > (start_dist + direct_distance), the shortcut saves time!
        steps_saved = end_dist - start_dist - direct_distance
        if steps_saved >= min_savings:
            yield start_pos, end_pos, steps_saved


def count_valid_shortcuts(input_path: str, max_length: int, min_savings: int) -> int:
    grid = read_grid(input_path)
    start_position = next(pos for pos, char in grid.items() if char == "S")
    distances = find_all_distances(grid, start_position)

    return len(list(find_valid_shortcuts(distances, max_length, min_savings)))


def solve_first(input_path: str) -> int:
    min_savings = 64 if input_path == "day_20_example.txt" else 100

    return count_valid_shortcuts(input_path, max_length=2, min_savings=min_savings)


def solve_second(input_path: str) -> int:
    min_savings = 50 if input_path == "day_20_example.txt" else 100

    return count_valid_shortcuts(input_path, max_length=20, min_savings=min_savings)
