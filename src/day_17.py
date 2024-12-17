from dataclasses import dataclass
from pathlib import Path

BITS = 3
MAX_OCTAL = (1 << BITS) - 1  # maximum value of one octal digit (7)


@dataclass
class VirtualMachine:
    accumulator_register: int
    general_purpose_register_b: int
    general_purpose_register_c: int
    program: list[int]
    instruction_pointer: int = 0
    output: list[int] = None

    def __post_init__(self) -> None:
        self.output = []

    def get_combo_value(self, operand: int) -> int:
        match operand:
            case x if x <= 3:
                return operand
            case 4:
                return self.accumulator_register
            case 5:
                return self.general_purpose_register_b
            case 6:
                return self.general_purpose_register_c
            case _:
                msg = f"Invalid combo operand: {operand}"

                raise ValueError(msg)

    def step(self) -> bool:
        if self.instruction_pointer >= len(self.program):
            return False

        opcode = self.program[self.instruction_pointer]
        operand = self.program[self.instruction_pointer + 1]

        match opcode:
            case 0:
                self.accumulator_register >>= self.get_combo_value(operand)
            case 1:
                self.general_purpose_register_b ^= operand
            case 2:
                self.general_purpose_register_b = (
                    self.get_combo_value(operand) & MAX_OCTAL
                )
            case 3:
                if self.accumulator_register != 0:
                    self.instruction_pointer = operand
                    return True
            case 4:
                self.general_purpose_register_b ^= self.general_purpose_register_c
            case 5:
                self.output.append(self.get_combo_value(operand) & MAX_OCTAL)
            case 6:
                self.general_purpose_register_b = (
                    self.accumulator_register >> self.get_combo_value(operand)
                )
            case 7:
                self.general_purpose_register_c = (
                    self.accumulator_register >> self.get_combo_value(operand)
                )

        self.instruction_pointer += 2

        return True


def read_input(filename: str) -> tuple[int, int, int, list[int]]:
    path = Path("in") / filename
    lines = path.read_text().strip().split("\n")

    a = int(lines[0].split(": ")[1])
    b = int(lines[1].split(": ")[1])
    c = int(lines[2].split(": ")[1])
    program = [int(x) for x in lines[4].split(": ")[1].split(",")]

    return a, b, c, program


def solve_first(filename: str) -> str:
    a, b, c, program = read_input(filename)
    vm = VirtualMachine(a, b, c, program)

    while vm.step():
        pass

    return ",".join(str(x) for x in vm.output)


def solve_second(filename: str) -> int:
    _, _, _, program = read_input(filename)

    numbers_to_try: list[tuple[int, int]] = [(1, 0)]  # start on right

    for digits_to_match, current_value in numbers_to_try:
        for next_value in range(current_value, current_value + MAX_OCTAL + 1):
            vm = VirtualMachine(next_value, 0, 0, program)
            while vm.step():
                pass

            # check if output matches the expected digits so far
            if vm.output == program[-digits_to_match:]:
                if digits_to_match == len(program):
                    return next_value

                # shift left by 3 bits to make room for next octal digit
                next_starting_value = next_value << BITS
                numbers_to_try.append((digits_to_match + 1, next_starting_value))

    msg = "No solution found"

    raise ValueError(msg)
