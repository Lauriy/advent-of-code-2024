from pathlib import Path


def parse_input(
    input_path: Path,
) -> tuple[dict[str, int], dict[str, tuple[str, str, str]]]:
    initial_values, gates = {}, {}

    sections = input_path.read_text().strip().split("\n\n")
    for line in sections[0].splitlines():
        wire, value = line.split(": ")
        initial_values[wire] = int(value)

    for line in sections[1].splitlines():
        inputs, output = line.split(" -> ")
        input1, operation, input2 = inputs.split()
        gates[output] = (input1, operation, input2)

    return initial_values, gates


def simulate_circuit(
    initial_values: dict[str, int],
    gates: dict[str, tuple[str, str, str]],
) -> dict[str, int]:
    wire_values = initial_values.copy()
    unresolved_gates = gates.copy()

    while unresolved_gates:
        progress_made = False

        for output_wire, (input1, operation, input2) in list(unresolved_gates.items()):
            # Skip if either input is unavailable
            if input1 not in wire_values or input2 not in wire_values:
                continue

            value1, value2 = wire_values[input1], wire_values[input2]

            if operation == "AND":
                wire_values[output_wire] = value1 & value2
            elif operation == "OR":
                wire_values[output_wire] = value1 | value2
            elif operation == "XOR":
                wire_values[output_wire] = value1 ^ value2

            # Successfully resolved this gate
            del unresolved_gates[output_wire]
            progress_made = True

        if not progress_made:
            unresolved_inputs = {
                (output_wire, input1, input2)
                for output_wire, (input1, _, input2) in unresolved_gates.items()
                if input1 not in wire_values or input2 not in wire_values
            }
            msg = f"Circuit evaluation could not progress further. Unresolved gates: {unresolved_inputs}"

            raise ValueError(
                msg,
            )

    return wire_values


def calculate_decimal_output(wire_values: dict[str, int]) -> int:
    z_wires = sorted(
        (wire for wire in wire_values if wire.startswith("z")),
        key=lambda wire: int(wire[1:]) if wire[1:].isdigit() else -1,
    )

    decimal_value = 0
    for wire in reversed(z_wires):
        decimal_value = (decimal_value << 1) | wire_values[wire]

    return decimal_value


def solve_first(filename: str) -> int:
    input_path = Path("in") / filename
    initial_values, gates = parse_input(input_path)
    wire_values = simulate_circuit(initial_values, gates)

    return calculate_decimal_output(wire_values)


def solve_second(filename: str) -> str:
    return "dunno"
