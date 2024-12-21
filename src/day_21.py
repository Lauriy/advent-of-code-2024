from functools import cache
from itertools import permutations
from pathlib import Path

NUMERIC_KEYPAD = ["789", "456", "123", " 0A"]
DIRECTIONAL_KEYPAD = [" ^A", "<v>"]
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
DIRECTION_SYMBOLS = dict(zip(DIRECTIONS, "^v<>", strict=False))


@cache
def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def read_input(filename: str) -> list[str]:
    input_path = Path(__file__).parent.parent / "in" / filename

    return input_path.read_text().splitlines()


@cache
def get_symbol_positions(keypad: tuple[str, ...]) -> dict[str, tuple[int, int]]:
    return {
        char: (row, col)
        for row, line in enumerate(keypad)
        for col, char in enumerate(line)
        if char != " "
    }


@cache
def find_shortest_path(
    code: str,
    keypad: tuple[str, ...],
    start_row: int,
    start_col: int,
) -> tuple[str, ...]:
    rows, cols = len(keypad), len(keypad[0])
    symbol_positions = get_symbol_positions(keypad)

    paths = []
    for direction_order in permutations(DIRECTIONS):
        path = []
        current_row, current_col = start_row, start_col

        for target_char in code:
            target_row, target_col = symbol_positions[target_char]

            while True:
                moved = False
                for delta_row, delta_col in direction_order:
                    new_row, new_col = current_row + delta_row, current_col + delta_col

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and keypad[new_row][new_col] != " "
                        and manhattan_distance(
                            target_row,
                            target_col,
                            current_row,
                            current_col,
                        )
                        > manhattan_distance(target_row, target_col, new_row, new_col)
                    ):
                        path.append(DIRECTION_SYMBOLS[delta_row, delta_col])
                        current_row, current_col = new_row, new_col
                        moved = True

                        break

                if not moved:
                    path.append("A")

                    break

        paths.append("".join(path))

    return tuple(paths)  # tuples can be cached


@cache
def calculate_path_length(code: str, depth: int = 0, max_depth: int = 2) -> int:
    if depth == max_depth:
        return len(code)

    chunks = code[:-1].split("A")
    total_length = 0

    for chunk in chunks:
        possible_paths = find_shortest_path(
            chunk + "A",
            tuple(DIRECTIONAL_KEYPAD),
            start_row=0,
            start_col=2,
        )
        min_chunk_length = min(
            calculate_path_length(
                path,
                depth=depth + 1,
                max_depth=max_depth,
            )
            for path in possible_paths
        )
        total_length += min_chunk_length

    return total_length


def solve_keypad_sequence(filename: str, max_depth: int) -> int:
    sequences = read_input(filename)

    total_complexity = 0
    for sequence in sequences:
        possible_paths = find_shortest_path(
            sequence,
            tuple(NUMERIC_KEYPAD),
            start_row=3,
            start_col=2,
        )
        min_sequence_length = min(
            calculate_path_length(
                path,
                depth=0,
                max_depth=max_depth,
            )
            for path in possible_paths
        )

        numeric_value = int("".join(char for char in sequence if char.isdigit()))
        total_complexity += min_sequence_length * numeric_value

    return total_complexity


def solve_first(filename: str) -> int:
    return solve_keypad_sequence(filename, max_depth=2)


def solve_second(filename: str) -> int:
    return solve_keypad_sequence(filename, max_depth=25)
