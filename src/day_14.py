from dataclasses import dataclass
from pathlib import Path

SIMULATION_WIDTH = 101
SIMULATION_HEIGHT = 103
EXAMPLE_WIDTH = 11
EXAMPLE_HEIGHT = 7
SIMULATION_STEPS = 10000


@dataclass
class Robot:
    pos: tuple[int, int]
    vel: tuple[int, int]


def parse_input(filename: str) -> list[Robot]:
    robots = []
    with Path(filename).open() as f:
        for line in f:
            p_part, v_part = line.strip().split()
            px, py = map(int, p_part[2:].split(","))
            vx, vy = map(int, v_part[2:].split(","))
            robots.append(Robot((px, py), (vx, vy)))

    return robots


def update_robot_positions(robots: list[Robot], width: int, height: int) -> None:
    for robot in robots:
        robot.pos = (
            (robot.pos[0] + robot.vel[0]) % width,
            (robot.pos[1] + robot.vel[1]) % height,
        )


def find_longest_vertical_line(
    points: set[tuple[int, int]],
    width: int,
    height: int,
) -> tuple[int, int]:
    max_length = best_x = 0

    for x in range(width):
        current_streak = 0
        for y in range(height):
            if (x, y) in points:
                current_streak += 1
                if current_streak > max_length:
                    max_length = current_streak
                    best_x = x
            else:
                current_streak = 0

    return max_length, best_x


def count_robots_by_quadrant(robots: list[Robot], width: int, height: int) -> list[int]:
    mid_x, mid_y = width // 2, height // 2
    quadrants = [0] * 4  # [top-left, top-right, bottom-left, bottom-right]

    for robot in robots:
        x, y = robot.pos
        if x == mid_x or y == mid_y:  # Skip robots on middle lines
            continue

        quadrants[int(x >= mid_x) + 2 * int(y >= mid_y)] += 1

    return quadrants


def solve_first(filename: str) -> int:
    robots = parse_input(filename)
    width = SIMULATION_WIDTH if "example" not in filename else EXAMPLE_WIDTH
    height = SIMULATION_HEIGHT if "example" not in filename else EXAMPLE_HEIGHT

    for _ in range(100):
        update_robot_positions(robots, width, height)

    quadrants = count_robots_by_quadrant(robots, width, height)
    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return safety_factor


def solve_second(filename: str) -> int:
    robots = parse_input(filename)
    width = SIMULATION_WIDTH if "example" not in filename else EXAMPLE_WIDTH
    height = SIMULATION_HEIGHT if "example" not in filename else EXAMPLE_HEIGHT

    max_vertical = best_time = 0

    for t in range(SIMULATION_STEPS):
        points = {r.pos for r in robots}
        current_max, best_x = find_longest_vertical_line(points, width, height)

        if current_max > max_vertical:
            max_vertical = current_max
            best_time = t
            print(f"\nNew best at {t} seconds: {current_max} at x={best_x}")  # noqa: T201
            for y in range(height):
                print("".join("#" if (x, y) in points else "." for x in range(width)))  # noqa: T201

        update_robot_positions(robots, width, height)

    return best_time
