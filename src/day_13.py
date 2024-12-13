import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ClawMachine:
    button_a_x: int
    button_a_y: int
    button_b_x: int
    button_b_y: int
    prize_x: int
    prize_y: int


def parse_input(filename: str) -> list[ClawMachine]:
    machines = []
    current_machine = {}

    for line in Path(filename).read_text().splitlines():
        if not line:
            continue

        if match := re.match(r"Button A: X\+(\d+), Y\+(\d+)", line):
            current_machine["button_a_x"] = int(match.group(1))
            current_machine["button_a_y"] = int(match.group(2))
        elif match := re.match(r"Button B: X\+(\d+), Y\+(\d+)", line):
            current_machine["button_b_x"] = int(match.group(1))
            current_machine["button_b_y"] = int(match.group(2))
        elif match := re.match(r"Prize: X=(\d+), Y=(\d+)", line):
            current_machine["prize_x"] = int(match.group(1))
            current_machine["prize_y"] = int(match.group(2))
            machines.append(ClawMachine(**current_machine))
            current_machine = {}

    return machines


def solve_machine(machine: ClawMachine) -> tuple[int, int] | None:
    a_x = machine.button_a_x
    a_y = machine.button_a_y
    b_x = machine.button_b_x
    b_y = machine.button_b_y
    p_x = machine.prize_x
    p_y = machine.prize_y

    det = a_x * b_y - b_x * a_y
    if det == 0:
        return None

    # Find x using Cramer's rule
    x = (p_x * b_y - b_x * p_y) // det
    if x < 0 or (p_x * b_y - b_x * p_y) % det != 0:
        return None

    # Find y using Cramer's rule
    y = (a_x * p_y - a_y * p_x) // det
    if y < 0 or (a_x * p_y - a_y * p_x) % det != 0:
        return None

    # Verify solution satisfies both equations
    if a_x * x + b_x * y != p_x or a_y * x + b_y * y != p_y:
        return None

    return (x, y)


def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return a_presses * 3 + b_presses


def solve_first(filename: str) -> int:
    total = 0
    for machine in parse_input(filename):
        if solution := solve_machine(machine):
            total += calculate_tokens(*solution)

    return total


def solve_second(filename: str) -> int:
    total = 0
    machines = parse_input(filename)

    offset = 10_000_000_000_000
    for machine in machines:
        offset_machine = ClawMachine(
            button_a_x=machine.button_a_x,
            button_a_y=machine.button_a_y,
            button_b_x=machine.button_b_x,
            button_b_y=machine.button_b_y,
            prize_x=machine.prize_x + offset,
            prize_y=machine.prize_y + offset,
        )
        if solution := solve_machine(offset_machine):
            total += calculate_tokens(*solution)

    return total
