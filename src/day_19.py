from pathlib import Path
from typing import NamedTuple


class TowelPatterns(NamedTuple):
    patterns: list[str]
    designs: list[str]


def read_input(filename: str) -> TowelPatterns:
    path = Path(__file__).parent.parent / "in" / filename
    patterns_str, designs_str = path.read_text().split("\n\n")
    patterns = [p.strip() for p in patterns_str.split(",")]
    designs = designs_str.strip().splitlines()

    return TowelPatterns(patterns, designs)


def can_make_design(
    design: str,
    patterns: list[str],
    memo: dict[str, bool] | None = None,
) -> bool:
    if memo is None:
        memo = {}

    if not design:
        return True

    if design in memo:
        return memo[design]

    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern) :]
            if can_make_design(remaining, patterns, memo):
                memo[design] = True

                return True

    memo[design] = False

    return False


def count_ways(
    design: str,
    patterns: list[str],
    memo: dict[str, int] | None = None,
) -> int:
    if memo is None:
        memo = {}

    if not design:
        return 1

    if design in memo:
        return memo[design]

    total = 0
    for pattern in patterns:
        if design.startswith(pattern):
            remaining = design[len(pattern) :]
            total += count_ways(remaining, patterns, memo)

    memo[design] = total

    return total


def solve_first(filename: str) -> int:
    data = read_input(filename)

    return sum(1 for design in data.designs if can_make_design(design, data.patterns))


def solve_second(filename: str) -> int:
    data = read_input(filename)

    return sum(count_ways(design, data.patterns) for design in data.designs)
