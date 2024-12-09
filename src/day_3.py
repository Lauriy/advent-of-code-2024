import re


def parse_mul_instructions(line, check_enabled=False):
    total = 0
    if not check_enabled:
        mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.finditer(mul_pattern, line)
        for match in matches:
            x = int(match.group(1))
            y = int(match.group(2))
            total += x * y

        return total

    enabled = True
    pos = 0
    line_buffer = ""  # Buffer for potential split instructions

    while pos < len(line):
        line[pos:]
        line_buffer += line[pos]

        if "do()" in line_buffer:
            enabled = True
            line_buffer = ""
            pos += 1
            continue

        if "don't()" in line_buffer:
            enabled = False
            line_buffer = ""
            pos += 1
            continue

        mul_match = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", line_buffer)
        if mul_match:
            if enabled:
                x = int(mul_match.group(1))
                y = int(mul_match.group(2))
                total += x * y
            line_buffer = line_buffer[mul_match.end() :]

        if len(line_buffer) > 20:  # Max length needed for a mul instruction
            line_buffer = line_buffer[-20:]

        pos += 1

    return total


def solve_first(file_name: str) -> int:
    total = 0
    with open(file_name) as f:
        for line in f:
            total += parse_mul_instructions(line.strip())

    return total


def solve_second(file_name: str) -> int:
    total = 0
    with open(file_name) as f:
        text = f.read()
        total += parse_mul_instructions(text, check_enabled=True)

    return total
