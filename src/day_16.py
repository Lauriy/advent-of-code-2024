from collections import deque
from pathlib import Path
from typing import NamedTuple


class State(NamedTuple):
    position: complex  # position as complex number (x + yi)
    direction: complex  # direction as unit vector: 1=east, 1j=south, -1=west, -1j=north


MOVE_COST = 1
TURN_COST = 1000


def parse_input(filename: str) -> tuple[set[complex], complex, complex]:
    lines = Path("in", filename).read_text().splitlines()
    walls = set()
    start_position = end_position = 0j

    for y_coord, line in enumerate(lines):
        for x_coord, char in enumerate(line):
            position = complex(x_coord, y_coord)
            if char == "#":
                walls.add(position)
            elif char == "S":
                start_position = position
            elif char == "E":
                end_position = position

    return walls, start_position, end_position


def find_path_info(
    walls: set[complex],
    start_position: complex,
    end_position: complex,
    find_all_paths: bool = False,
) -> tuple[int, set[complex]]:
    initial_state = State(start_position, 1)  # start facing east
    queue = deque([initial_state])
    costs = {initial_state: 0}

    while queue:
        current_state = queue.popleft()
        if current_state.position == end_position:
            continue

        # try moving forward
        new_position = current_state.position + current_state.direction
        if new_position not in walls:
            new_state = State(new_position, current_state.direction)
            new_cost = costs[current_state] + MOVE_COST
            if new_state not in costs or new_cost < costs[new_state]:
                costs[new_state] = new_cost
                queue.append(new_state)

        # try turning left/right (multiply direction by ±i)
        for rotation in (1j, -1j):
            new_direction = current_state.direction * rotation
            new_state = State(current_state.position, new_direction)
            new_cost = costs[current_state] + TURN_COST
            if new_state not in costs or new_cost < costs[new_state]:
                costs[new_state] = new_cost
                queue.append(new_state)

    end_states = [state for state in costs if state.position == end_position]
    if not end_states:
        return 0, set()

    min_cost = min(costs[state] for state in end_states)
    if not find_all_paths:
        return min_cost, set()

    optimal_tiles = {end_position}
    queue = deque([State(end_position, direction) for direction in (1, 1j, -1, -1j)])
    reverse_costs = {
        State(end_position, direction): min_cost for direction in (1, 1j, -1, -1j)
    }

    while queue:
        current_state = queue.popleft()
        current_cost = reverse_costs[current_state]

        # try moving backward
        prev_position = current_state.position - current_state.direction
        if prev_position not in walls:
            prev_state = State(prev_position, current_state.direction)
            prev_cost = current_cost - MOVE_COST
            if (
                prev_state in costs
                and costs[prev_state] == prev_cost
                and prev_state not in reverse_costs
            ):
                optimal_tiles.add(prev_position)
                reverse_costs[prev_state] = prev_cost
                queue.append(prev_state)

        # try coming from either rotation
        for rotation in (1j, -1j):
            prev_direction = current_state.direction * rotation
            prev_state = State(current_state.position, prev_direction)
            prev_cost = current_cost - TURN_COST
            if (
                prev_state in costs
                and costs[prev_state] == prev_cost
                and prev_state not in reverse_costs
            ):
                reverse_costs[prev_state] = prev_cost
                queue.append(prev_state)

    return min_cost, optimal_tiles


def solve_first(filename: str) -> int:
    walls, start_position, end_position = parse_input(filename)
    min_cost, _ = find_path_info(walls, start_position, end_position)

    return min_cost


def solve_second(filename: str) -> int:
    walls, start_position, end_position = parse_input(filename)
    _, optimal_tiles = find_path_info(
        walls,
        start_position,
        end_position,
        find_all_paths=True,
    )

    return len(optimal_tiles)
