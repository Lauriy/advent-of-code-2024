from functools import cache
from itertools import combinations
from pathlib import Path

LOGICAL_AND = "AND"
LOGICAL_OR = "OR"
LOGICAL_XOR = "XOR"


def parse_input_file(
    input_file_path: Path,
) -> tuple[dict[str, int], dict[str, tuple[str, str, str]]]:
    initial_wire_values, logic_gates = {}, {}
    sections = input_file_path.read_text().strip().split("\n\n")

    for line in sections[0].splitlines():
        wire, value = line.split(": ")
        initial_wire_values[wire] = int(value)

    for line in sections[1].splitlines():
        inputs, output = line.split(" -> ")
        input1, operation, input2 = inputs.split()
        logic_gates[output] = (input1, operation, input2)

    return initial_wire_values, logic_gates


def evaluate_circuit(
    initial_wire_values: dict[str, int],
    logic_gates: dict[str, tuple[str, str, str]],
) -> dict[str, int]:
    resolved_wire_values = initial_wire_values.copy()
    unresolved_gates = logic_gates.copy()

    while unresolved_gates:
        progress_made = False

        for output_wire, (input1, operation, input2) in list(unresolved_gates.items()):
            if input1 not in resolved_wire_values or input2 not in resolved_wire_values:
                continue

            value1, value2 = resolved_wire_values[input1], resolved_wire_values[input2]
            resolved_wire_values[output_wire] = perform_logic_operation(
                value1,
                value2,
                operation,
            )
            del unresolved_gates[output_wire]
            progress_made = True

        if not progress_made:
            unresolved_inputs = {
                (output_wire, input1, input2)
                for output_wire, (input1, _, input2) in unresolved_gates.items()
                if input1 not in resolved_wire_values
                or input2 not in resolved_wire_values
            }
            msg = f"Circuit evaluation could not progress further. Unresolved gates: {unresolved_inputs}"
            raise ValueError(msg)

    return resolved_wire_values


def perform_logic_operation(value1: int, value2: int, operation: str) -> int:
    if operation == LOGICAL_AND:
        return value1 & value2
    if operation == LOGICAL_OR:
        return value1 | value2
    if operation == LOGICAL_XOR:
        return value1 ^ value2
    msg = f"Unknown operation: {operation}"
    raise ValueError(msg)


def calculate_decimal_output(resolved_wire_values: dict[str, int]) -> int:
    z_wires = sorted(
        (wire for wire in resolved_wire_values if wire.startswith("z")),
        key=lambda wire: int(wire[1:]) if wire[1:].isdigit() else -1,
    )

    decimal_value = 0
    for wire in reversed(z_wires):
        decimal_value = (decimal_value << 1) | resolved_wire_values[wire]

    return decimal_value


def convert_gates_to_operation_list(
    logic_gates: dict[str, tuple[str, str, str]],
) -> list[tuple[str, str, str, str]]:
    return [
        (input1, input2, output, operation)
        for output, (input1, operation, input2) in logic_gates.items()
    ]


@cache  # Cache results of this function
def find_furthest_progress(
    operation_list: tuple[tuple[str, str, str, str]],
) -> tuple[int, set[str]]:
    operations = {
        (frozenset([input1, input2]), operation): result
        for input1, input2, result, operation in operation_list
    }
    carries = {}
    correct_wires = set()
    previous_intermediates = set()

    for position in range(46):
        formatted_position = f"0{position}" if position < 10 else str(position)
        predicted_digit = operations.get(
            (
                frozenset([f"x{formatted_position}", f"y{formatted_position}"]),
                LOGICAL_XOR,
            ),
        )
        previous_carry = operations.get(
            (
                frozenset([f"x{formatted_position}", f"y{formatted_position}"]),
                LOGICAL_AND,
            ),
        )

        if position == 0:
            if predicted_digit != "z00":
                return 0, correct_wires
            carries[position] = previous_carry
            continue

        current_digit = operations.get(
            (frozenset([carries[position - 1], predicted_digit]), LOGICAL_XOR),
        )
        if current_digit != f"z{formatted_position}":
            return position - 1, correct_wires

        correct_wires.update(
            {carries[position - 1], predicted_digit, *previous_intermediates},
        )
        next_carry = operations.get(
            (frozenset([carries[position - 1], predicted_digit]), LOGICAL_AND),
        )
        carry_out = operations.get(
            (frozenset([previous_carry, next_carry]), LOGICAL_OR),
        )
        carries[position] = carry_out
        previous_intermediates = {previous_carry, next_carry}

    return 45, correct_wires


def solve_first(filename: str) -> int:
    input_path = Path("in") / filename
    initial_values, gates = parse_input_file(input_path)
    wire_values = evaluate_circuit(initial_values, gates)

    return calculate_decimal_output(wire_values)


def solve_second(filename: str) -> str:
    input_path = Path("in") / filename
    _, gates = parse_input_file(input_path)

    operation_list = convert_gates_to_operation_list(gates)
    swaps = set()

    base, base_used = find_furthest_progress(
        tuple(operation_list),
    )  # Convert to tuple for caching

    for _ in range(4):
        best_swap = None
        best_improvement = base

        for i, j in combinations(range(len(operation_list)), 2):
            input1_i, input2_i, result_i, operation_i = operation_list[i]
            input1_j, input2_j, result_j, operation_j = operation_list[j]

            if (
                "z00" in (result_i, result_j)
                or result_i in base_used
                or result_j in base_used
            ):
                continue

            operation_list[i] = (input1_i, input2_i, result_j, operation_i)
            operation_list[j] = (input1_j, input2_j, result_i, operation_j)

            attempt, attempt_used = find_furthest_progress(
                tuple(operation_list),
            )  # Convert to tuple for caching
            if attempt > best_improvement:
                best_improvement = attempt
                best_swap = (result_i, result_j)

            operation_list[i] = (input1_i, input2_i, result_i, operation_i)
            operation_list[j] = (input1_j, input2_j, result_j, operation_j)

        if best_swap:
            swaps.add(best_swap)
            base = best_improvement
            for index in range(len(operation_list)):
                if operation_list[index][2] == best_swap[0]:
                    input1, input2, _, operation = operation_list[index]
                    operation_list[index] = (input1, input2, best_swap[1], operation)
                elif operation_list[index][2] == best_swap[1]:
                    input1, input2, _, operation = operation_list[index]
                    operation_list[index] = (input1, input2, best_swap[0], operation)

    return ",".join(sorted(sum(swaps, ())))
