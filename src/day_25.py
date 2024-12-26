from pathlib import Path


def parse_schematic(schematic: str) -> list[int]:
    lines = schematic.strip().splitlines()
    heights = []

    for col in range(len(lines[0])):
        if lines[0][col] == "#":
            height = 0
            for row in range(len(lines)):
                if lines[row][col] == ".":
                    break
                height += 1
            heights.append(height - 1)
        else:
            height = 0
            for row in range(len(lines) - 1, -1, -1):
                if lines[row][col] == ".":
                    break
                height += 1
            heights.append(height - 1)

    return heights


def read_schematics(input_path: Path) -> tuple[list[list[int]], list[list[int]]]:
    locks, keys = [], []
    for schematic in input_path.read_text().strip().split("\n\n"):
        heights = parse_schematic(schematic)
        if schematic.splitlines()[0].startswith("#"):
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys


def can_fit(lock: list[int], key: list[int], space: int = 6) -> bool:
    return all(lock[i] + key[i] < space for i in range(len(lock)))


def solve_first(filename: str) -> int:
    input_path = Path(__file__).parent.parent / "in" / filename
    locks, keys = read_schematics(input_path)

    return sum(
        1
        for lock in locks
        for key in keys
        if can_fit(lock, key)
    )



def solve_second(filename: str) -> str:
    return "Not implemented"
