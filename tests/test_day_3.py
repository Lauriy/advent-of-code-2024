from src.day_3 import parse_mul_instructions
from src.day_3 import solve_first
from src.day_3 import solve_second


def test_parse_mul_instructions() -> None:
    assert parse_mul_instructions("mul(2,4)") == 8
    assert parse_mul_instructions("mul(123,4)") == 492

    assert parse_mul_instructions("mul(2,4)mul(3,5)") == 23  # 8 + 15

    assert parse_mul_instructions("mul(4*") == 0
    assert parse_mul_instructions("mul[3,7]") == 0
    assert parse_mul_instructions("?(12,34)") == 0
    assert parse_mul_instructions("mul ( 2 , 4 )") == 0


def test_parse_mul_instructions_with_conditionals() -> None:
    assert parse_mul_instructions("mul(2,4)", check_enabled=True) == 8
    assert parse_mul_instructions("don't()mul(2,4)", check_enabled=True) == 0
    assert (
        parse_mul_instructions("don't()mul(2,4)do()mul(3,5)", check_enabled=True) == 15
    )

    example = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"
    assert parse_mul_instructions(example, check_enabled=True) == 48  # 2*4 + 8*5

    assert (
        parse_mul_instructions(
            "mul(2,3)don't()mul(4,5)don't()mul(6,7)",
            check_enabled=True,
        )
        == 6
    )  # Only first mul
    assert (
        parse_mul_instructions(
            "do()mul(2,3)don't()mul(4,5)do()mul(6,7)",
            check_enabled=True,
        )
        == 48
    )  # First and last
    assert (
        parse_mul_instructions(
            "don't()mul(2,3)mul(4,5)do()mul(6,7)",
            check_enabled=True,
        )
        == 42
    )  # Only last


def test_solve_first_example() -> None:
    assert solve_first("in/day_3_example_1.txt") == 161


def test_solve_first() -> None:
    result = solve_first("in/day_3.txt")
    assert result == 155955228


def test_solve_second_example() -> None:
    assert solve_second("in/day_3_example_2.txt") == 48


def test_solve_second() -> None:
    result = solve_second("in/day_3.txt")
    assert result == 100189366
