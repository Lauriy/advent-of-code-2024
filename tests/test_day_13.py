from src.day_13 import ClawMachine
from src.day_13 import calculate_tokens
from src.day_13 import parse_input
from src.day_13 import solve_first
from src.day_13 import solve_machine
from src.day_13 import solve_second


def test_parse_input() -> None:
    machines = parse_input("in/day_13_example.txt")
    assert len(machines) == 4

    first_machine = machines[0]
    assert first_machine.button_a_x == 94
    assert first_machine.button_a_y == 34
    assert first_machine.button_b_x == 22
    assert first_machine.button_b_y == 67
    assert first_machine.prize_x == 8400
    assert first_machine.prize_y == 5400


def test_solve_machine() -> None:
    machine = ClawMachine(
        button_a_x=94,
        button_a_y=34,
        button_b_x=22,
        button_b_y=67,
        prize_x=8400,
        prize_y=5400,
    )
    solution = solve_machine(machine)
    assert solution == (80, 40)

    machine = ClawMachine(
        button_a_x=26,
        button_a_y=66,
        button_b_x=67,
        button_b_y=21,
        prize_x=12748,
        prize_y=12176,
    )
    assert solve_machine(machine) is None


def test_calculate_tokens() -> None:
    assert calculate_tokens(80, 40) == 280
    assert calculate_tokens(38, 86) == 200


def test_solve_first_example() -> None:
    assert solve_first("in/day_13_example.txt") == 480


def test_solve_first() -> None:
    assert solve_first("in/day_13.txt") == 34393


def test_solve_second_example() -> None:
    assert solve_second("in/day_13_example.txt") == 875318608908


def test_solve_second() -> None:
    assert solve_second("in/day_13.txt") == 83551068361379
