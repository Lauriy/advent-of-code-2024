from typing import List, Set, Dict, Tuple, Optional, Callable
from collections import defaultdict


def get_vector(p1: Tuple[int, int], p2: Tuple[int, int]) -> Tuple[int, int]:
    return (p2[0] - p1[0], p2[1] - p1[1])


def dot_product(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
    return v1[0] * v2[0] + v1[1] * v2[1]


def cross_product(v1: Tuple[int, int], v2: Tuple[int, int]) -> int:
    return v1[0] * v2[1] - v1[1] * v2[0]


def is_collinear(p1: Tuple[int, int], p2: Tuple[int, int], p3: Tuple[int, int]) -> bool:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1)


def distance_squared(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x1, y1 = p1
    x2, y2 = p2

    return (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)


def has_double_distance(p: Tuple[int, int], a1: Tuple[int, int], a2: Tuple[int, int]) -> bool:
    d1 = distance_squared(p, a1)
    d2 = distance_squared(p, a2)
    
    # Skip if antenna
    if d1 == 0 or d2 == 0:
        return False
        
    return d1 == 4 * d2 or d2 == 4 * d1


def find_antinodes(grid: List[str], antennas: Dict[str, List[Tuple[int, int]]], 
                  is_valid_point: Callable[[Tuple[int, int], Tuple[int, int], Tuple[int, int]], bool],
                  include_antennas: bool = False) -> set:
    antinodes = set()
    height = len(grid)
    width = len(grid[0])
    
    for positions in antennas.values():
        if len(positions) < 2:
            continue
            
        if include_antennas:
            antinodes.update(positions)
        
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                a1 = positions[i]
                a2 = positions[j]
                
                for y in range(height):
                    for x in range(width):
                        p = (x, y)
                        if is_valid_point(p, a1, a2):
                            antinodes.add(p)
    
    return antinodes


def find_antennas(grid: List[str]) -> Dict[str, List[Tuple[int, int]]]:
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                antennas[grid[y][x]].append((x, y))

    return antennas


def is_valid_part1(p: Tuple[int, int], a1: Tuple[int, int], a2: Tuple[int, int]) -> bool:
    return is_collinear(a1, a2, p) and has_double_distance(p, a1, a2)


def is_valid_part2(p: Tuple[int, int], a1: Tuple[int, int], a2: Tuple[int, int]) -> bool:
    return is_collinear(a1, a2, p)


def solve_first(filename: str) -> int:
    with open(filename) as f:
        grid = [line.strip() for line in f.readlines()]
    
    antennas = find_antennas(grid)
    antinodes = find_antinodes(grid, antennas, is_valid_part1)

    return len(antinodes)


def solve_second(filename: str) -> int:
    with open(filename) as f:
        grid = [line.strip() for line in f.readlines()]
    
    antennas = find_antennas(grid)
    antinodes = find_antinodes(grid, antennas, is_valid_part2, include_antennas=True)
    
    return len(antinodes)
