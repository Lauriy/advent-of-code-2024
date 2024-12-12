from collections import deque
from pathlib import Path

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input(input_path: str) -> list[list[str]]:
    return [list(line.strip()) for line in Path(input_path).read_text().splitlines()]


def get_neighbors(row: int, column: int) -> list[tuple[int, int]]:
    return [(row + move_row, column + move_col) for move_row, move_col in DIRECTIONS]


def is_valid_cell(row: int, column: int, height: int, width: int) -> bool:
    return 0 <= row < height and 0 <= column < width


def find_regions(grid: list[list[str]]) -> dict[tuple[str, int], set[tuple[int, int]]]:
    height = len(grid)
    width = len(grid[0])
    seen_cells = set()
    all_regions = {}
    letter_count = {}

    for row in range(height):
        for column in range(width):
            current_cell = (row, column)
            if current_cell in seen_cells:
                continue

            letter = grid[row][column]
            letter_count[letter] = letter_count.get(letter, 0) + 1
            region_name = (letter, letter_count[letter])

            # Find all connected cells with the same letter
            current_region = set()
            cells_to_check = deque([current_cell])

            while cells_to_check:
                check_row, check_col = cells_to_check.popleft()
                if (check_row, check_col) in seen_cells:
                    continue

                seen_cells.add((check_row, check_col))
                current_region.add((check_row, check_col))

                for neighbor_row, neighbor_col in get_neighbors(check_row, check_col):
                    neighbor_cell = (neighbor_row, neighbor_col)
                    if (
                        is_valid_cell(neighbor_row, neighbor_col, height, width)
                        and grid[neighbor_row][neighbor_col] == letter
                        and neighbor_cell not in seen_cells
                    ):
                        cells_to_check.append(neighbor_cell)

            all_regions[region_name] = current_region

    return all_regions


def calculate_perimeter(region: set[tuple[int, int]], grid: list[list[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    total_edges = 0

    for row, column in region:
        cell_letter = grid[row][column]
        for neighbor_row, neighbor_col in get_neighbors(row, column):
            if (
                not is_valid_cell(neighbor_row, neighbor_col, height, width)
                or grid[neighbor_row][neighbor_col] != cell_letter
            ):
                total_edges += 1

    return total_edges


def count_sides(
    region: set[tuple[int, int]],
    grid: list[list[str]],
    debug: bool = False,
) -> int:
    height = len(grid)
    width = len(grid[0])
    row, col = next(iter(region))
    cell_letter = grid[row][col]

    if debug:
        print(f"\nCounting sides for region {cell_letter} with area {len(region)}")  # noqa: T201

    # Find edges with their directions
    edges = set()
    for row, col in region:
        for move_row, move_col in DIRECTIONS:
            neighbor_row = row + move_row
            neighbor_col = col + move_col

            if (
                not is_valid_cell(neighbor_row, neighbor_col, height, width)
                or grid[neighbor_row][neighbor_col] != cell_letter
            ):
                edges.add((row, col, move_row, move_col))

    # Count unique sides by checking if adjacent cells share the edge
    sides = 0
    for row, col, move_row, move_col in edges:
        # A side is unique if cells to the right and below don't share it
        if (row + 1, col, move_row, move_col) not in edges and (
            row,
            col + 1,
            move_row,
            move_col,
        ) not in edges:
            sides += 1
            if debug:
                print(  # noqa: T201
                    f"Found unique side at ({row}, {col}) in direction ({move_row}, {move_col})",
                )

    if debug:
        print(f"Total sides: {sides}")  # noqa: T201

    return sides


def solve_first(input_path: str) -> int:
    grid = parse_input(input_path)
    regions = find_regions(grid)

    return sum(
        len(region) * calculate_perimeter(region, grid) for region in regions.values()
    )


def solve_second(input_path: str, debug: bool = False) -> int:
    grid = parse_input(input_path)
    regions = find_regions(grid)

    total = 0
    for region in regions.values():
        area = len(region)
        sides = count_sides(region, grid, debug)
        total += area * sides
        if debug:
            letter = grid[next(iter(region))[0]][next(iter(region))[1]]
            print(  # noqa: T201
                f"Region {letter}: area {area} × sides {sides} = price {area * sides}",
            )

    return total
