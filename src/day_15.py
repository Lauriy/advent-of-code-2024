from dataclasses import dataclass
from itertools import chain
from pathlib import Path


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, multiplier: int) -> "Point":
        return Point(self.x * multiplier, self.y * multiplier)

    def __hash__(self) -> int:
        return hash((self.x, self.y))


DIRECTIONS = {
    "<": Point(-1, 0),
    "^": Point(0, -1),
    ">": Point(1, 0),
    "v": Point(0, 1),
}


def parse_input(filename: str) -> tuple[str, str]:
    content = (Path(__file__).parent.parent / "in" / filename).read_text()
    grid, moves = content.strip().split("\n\n")

    return grid, moves


def make_grid(lines: list[str]) -> dict[Point, str]:
    return {
        Point(x, y): char for y, line in enumerate(lines) for x, char in enumerate(line)
    }


def solve_first(filename: str) -> int:
    grid_data, move_instructions = parse_input(filename)
    grid_mapping = make_grid(grid_data.split("\n"))
    box_positions = {point for point, char in grid_mapping.items() if char == "O"}
    wall_positions = {point for point, char in grid_mapping.items() if char == "#"}
    robot_position = next(point for point, char in grid_mapping.items() if char == "@")

    for move in move_instructions.strip():
        if move not in DIRECTIONS:  # avoid \n
            continue

        direction = DIRECTIONS[move]
        displaced_boxes = set()
        offset = 0

        while (
            next_position := robot_position + direction * (offset + 1)
        ) not in wall_positions and next_position in box_positions:
            displaced_boxes.add(next_position)
            offset += 1

        if next_position not in wall_positions:
            robot_position += direction
            box_positions -= displaced_boxes
            box_positions |= {box + direction for box in displaced_boxes}

    return sum(100 * box.y + box.x for box in box_positions)


@dataclass
class Box:
    left_position: Point
    width: int = 2

    def __post_init__(self) -> None:
        self.positions: list[Point] = [
            self.left_position + Point(offset, 0) for offset in range(self.width)
        ]

    def __contains__(self, point: Point) -> bool:
        return point in self.positions

    def __add__(self, direction: Point) -> "Box":
        return Box(self.left_position + direction, self.width)

    def __hash__(self) -> int:
        return hash(tuple(self.positions))


def solve_second(filename: str) -> int:
    grid_data, move_instructions = parse_input(filename)
    adjusted_grid = (
        grid_data.replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")
    )
    grid_mapping = make_grid(adjusted_grid.split("\n"))
    wide_boxes = {Box(point) for point, char in grid_mapping.items() if char == "["}
    wall_positions = {point for point, char in grid_mapping.items() if char == "#"}
    robot_position = next(point for point, char in grid_mapping.items() if char == "@")

    for move in move_instructions.strip():
        if move not in DIRECTIONS:
            continue

        direction = DIRECTIONS[move]
        displaced_boxes = set()

        if direction.x != 0:  # Horizontal movement
            offset = 0
            while (
                valid_position := (
                    current_position := robot_position + direction * (offset + 1)
                )
                not in wall_positions
            ) and (
                blocking_box := next(
                    (box for box in wide_boxes if current_position in box),
                    None,
                )
            ):
                if blocking_box:
                    displaced_boxes.add(blocking_box)
                offset += 2
        else:  # Vertical movement
            candidates = {robot_position}
            while (
                valid_position := all(
                    candidate + direction not in wall_positions
                    for candidate in candidates
                )
            ) and (
                blocking_boxes := {
                    box
                    for box in wide_boxes
                    if any(candidate + direction in box for candidate in candidates)
                }
            ):
                if blocking_boxes:
                    displaced_boxes.update(blocking_boxes)
                    candidates = set(
                        chain.from_iterable(box.positions for box in blocking_boxes),
                    )

        if valid_position:
            robot_position += direction
            wide_boxes -= displaced_boxes
            wide_boxes |= {box + direction for box in displaced_boxes}

    return sum(100 * box.left_position.y + box.left_position.x for box in wide_boxes)
