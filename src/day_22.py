from collections import defaultdict
from functools import cache
from itertools import pairwise
from pathlib import Path

SECRET_ITERATIONS = 2000


def read_input(filename: str) -> list[int]:
    input_path = Path(__file__).parent.parent / "in" / filename

    return [int(line) for line in input_path.read_text().splitlines()]


@cache
def secret_function(secret: int) -> int:
    # x % 16777216 = x & 0xFFFFFF (keep only the lowest 24 bits)
    # Step 1: XOR with (secret * 64) % 16777216
    secret = (secret ^ ((secret << 6) & 0xFFFFFF)) & 0xFFFFFF

    # Step 2: XOR with (secret // 32) % 16777216
    secret = (secret ^ (secret >> 5)) & 0xFFFFFF

    # Step 3: XOR with (secret * 2048) % 16777216
    return (secret ^ ((secret << 11) & 0xFFFFFF)) & 0xFFFFFF


def solve_first(filename: str) -> int:
    initial_secrets = read_input(filename)
    answer = 0
    for initial_secret in initial_secrets:
        secret_sequence = [initial_secret]
        for _ in range(SECRET_ITERATIONS):
            next_secret = secret_function(secret_sequence[-1])
            secret_sequence.append(next_secret)
        answer += next_secret

    return answer


def solve_second(filename: str) -> int:
    initial_secrets = read_input(filename)
    first_sighting_values_map = defaultdict(int)
    for initial_secret in initial_secrets:
        secret_sequence = [initial_secret]
        for _ in range(SECRET_ITERATIONS):
            next_secret = secret_function(secret_sequence[-1])
            secret_sequence.append(next_secret)
        last_digit_differences = [
            next_secret % 10 - previous_secret % 10
            for previous_secret, next_secret in pairwise(secret_sequence)
        ]
        first_sightings = set()
        for i in range(len(secret_sequence) - 4):
            four_tuple_of_diff = tuple(last_digit_differences[i : i + 4])
            if four_tuple_of_diff not in first_sightings:
                first_sightings.add(four_tuple_of_diff)
                # sell at end of sequence - is this a take on Technical Analysis? : )
                first_sighting_values_map[four_tuple_of_diff] += (
                    secret_sequence[i + 4] % 10
                )

    return max(first_sighting_values_map.values())
