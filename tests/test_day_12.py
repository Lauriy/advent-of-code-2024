from src.day_12 import calculate_perimeter
from src.day_12 import count_sides
from src.day_12 import find_regions
from src.day_12 import parse_input
from src.day_12 import solve_first
from src.day_12 import solve_second


def test_find_regions_example_1() -> None:
    grid = parse_input("in/day_12_example_1.txt")
    regions = find_regions(grid)

    assert len(regions) == 5  # A, B, C, D, E

    region_a = regions[("A", 1)]
    assert len(region_a) == 4

    region_b = regions[("B", 1)]
    assert len(region_b) == 4

    region_c = regions[("C", 1)]
    assert len(region_c) == 4

    region_d = regions[("D", 1)]
    assert len(region_d) == 1

    region_e = regions[("E", 1)]
    assert len(region_e) == 3


def test_calculate_perimeter_example_1() -> None:
    grid = parse_input("in/day_12_example_1.txt")
    regions = find_regions(grid)

    assert calculate_perimeter(regions[("A", 1)], grid) == 10
    assert calculate_perimeter(regions[("B", 1)], grid) == 8
    assert calculate_perimeter(regions[("C", 1)], grid) == 10
    assert calculate_perimeter(regions[("D", 1)], grid) == 4
    assert calculate_perimeter(regions[("E", 1)], grid) == 8


def test_solve_first_example_1() -> None:
    assert solve_first("in/day_12_example_1.txt") == 140


def test_solve_first_example_2() -> None:
    assert solve_first("in/day_12_example_2.txt") == 772


def test_solve_first_example_3() -> None:
    assert solve_first("in/day_12_example_3.txt") == 1930


def test_solve_first() -> None:
    assert solve_first("in/day_12.txt") == 1477924


def test_count_sides_example_1() -> None:
    grid = parse_input("in/day_12_example_1.txt")
    regions = find_regions(grid)

    assert count_sides(regions[("A", 1)], grid) == 4
    assert count_sides(regions[("B", 1)], grid) == 4
    assert count_sides(regions[("C", 1)], grid) == 8  # L
    assert count_sides(regions[("D", 1)], grid) == 4
    assert count_sides(regions[("E", 1)], grid) == 4


def test_solve_second_example_1() -> None:
    assert solve_second("in/day_12_example_1.txt", debug=True) == 80


def test_solve_second_example_2() -> None:
    assert solve_second("in/day_12_example_2.txt", debug=True) == 436


def test_solve_second_example_3() -> None:
    assert solve_second("in/day_12_example_3.txt", debug=True) == 1206


def test_solve_second_example_4() -> None:
    assert solve_second("in/day_12_example_4.txt", debug=True) == 236


def test_solve_second_example_5() -> None:
    assert solve_second("in/day_12_example_5.txt", debug=True) == 368


def test_solve_second() -> None:
    assert solve_second("in/day_12.txt") == 841934
