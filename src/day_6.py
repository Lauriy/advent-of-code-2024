from pathlib import Path
from typing import List, Set, Tuple, Dict
from enum import Enum
from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from copy import deepcopy
import logging
from threading import current_thread
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def turn_right(self) -> 'Direction':
        directions = list(Direction)
        current_index = directions.index(self)

        return directions[(current_index + 1) % 4]

def parse_input(input_text: str) -> Tuple[List[List[str]], Tuple[int, int], Direction]:
    grid = [list(line) for line in input_text.strip().splitlines()]
    start_pos = None
    start_dir = None
    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '^':
                start_pos = (x, y)
                start_dir = Direction.UP
                grid[y][x] = '.'
            elif grid[y][x] == '>':
                start_pos = (x, y)
                start_dir = Direction.RIGHT
                grid[y][x] = '.'
            elif grid[y][x] == 'v':
                start_pos = (x, y)
                start_dir = Direction.DOWN
                grid[y][x] = '.'
            elif grid[y][x] == '<':
                start_pos = (x, y)
                start_dir = Direction.LEFT
                grid[y][x] = '.'
    
    return grid, start_pos, start_dir

def is_inside_grid(pos: Tuple[int, int], grid: List[List[str]]) -> bool:
    x, y = pos

    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

def get_next_position(pos: Tuple[int, int], direction: Direction) -> Tuple[int, int]:
    dx, dy = direction.value
    x, y = pos

    return (x + dx, y + dy)

def get_unobstructed_path(grid: List[List[str]], start_pos: Tuple[int, int], start_dir: Direction) -> List[Tuple[Tuple[int, int], Direction]]:
    pos = start_pos
    direction = start_dir
    path = [(pos, direction)]
    visited_states = {(pos, direction)}
    
    while True:
        next_pos = get_next_position(pos, direction)
        
        if not is_inside_grid(next_pos, grid):
            break
            
        if grid[next_pos[1]][next_pos[0]] == '#':
            direction = direction.turn_right()
            state = (pos, direction)
            if state in visited_states:
                break
            path.append(state)
            visited_states.add(state)
            continue
            
        pos = next_pos
        state = (pos, direction)
        if state in visited_states:
            break
        path.append(state)
        visited_states.add(state)
    
    return path

def has_cycle_with_steps(grid: List[List[str]], start_state: Tuple[Tuple[int, int], Direction], max_steps: int = 1000) -> bool:
    visited = {}
    pos, direction = start_state
    current_state = start_state
    
    for step in range(max_steps):
        if current_state in visited:
            cycle_length = step - visited[current_state]
            if cycle_length <= max_steps // 2:
                return True

            return False
            
        visited[current_state] = step
        pos, direction = current_state
        
        next_pos = get_next_position(pos, direction)
        
        if not is_inside_grid(next_pos, grid):
            return False
            
        if grid[next_pos[1]][next_pos[0]] == '#':
            direction = direction.turn_right()
            current_state = (pos, direction)
        else:
            current_state = (next_pos, direction)
    
    return False

@dataclass(frozen=True)
class GridState:
    pos: Tuple[int, int]
    direction: Direction

def check_position_creates_loop(args: Tuple[List[List[str]], Tuple[int, int], Tuple[int, int], Direction, bool]) -> bool:
    grid, pos, start_pos, start_dir, debug = args
    x, y = pos
    thread_name = current_thread().name
    
    if grid[y][x] != '.' or pos == start_pos:
        return False
    
    logger.debug(f"{thread_name}: Checking position ({x}, {y})")
    
    # Make a copy of the grid for this thread
    local_grid = deepcopy(grid)
    local_grid[y][x] = '#'
    
    curr_pos = start_pos
    curr_dir = start_dir
    
    while True:
        next_pos = get_next_position(curr_pos, curr_dir)
        
        if next_pos == (x, y):
            break
            
        if not is_inside_grid(next_pos, local_grid):
            logger.debug(f"{thread_name}: Path escapes grid before hitting obstacle at ({x}, {y})")
            
            return False
            
        if local_grid[next_pos[1]][next_pos[0]] == '#':
            curr_dir = curr_dir.turn_right()
        else:
            curr_pos = next_pos
    
    # Check for a cycle from the obstacle point
    start_state = GridState(curr_pos, curr_dir)
    visited = {start_state: 0}
    curr_state = start_state
    step = 0
    max_steps = len(local_grid) * len(local_grid[0]) * 4  # width x height x 4 directions
    
    while step < max_steps:
        step += 1
        next_pos = get_next_position(curr_state.pos, curr_state.direction)
        
        if not is_inside_grid(next_pos, local_grid):
            logger.debug(f"{thread_name}: Path escapes grid after {step} steps at ({x}, {y})")
            
            return False
            
        if local_grid[next_pos[1]][next_pos[0]] == '#':
            next_state = GridState(curr_state.pos, curr_state.direction.turn_right())
        else:
            next_state = GridState(next_pos, curr_state.direction)
            
        if next_state in visited:
            cycle_length = step - visited[next_state]
            if cycle_length <= max_steps // 2:
                if debug:
                    print(f"Found loop at ({x}, {y}) affecting state at {curr_state.pos} facing {curr_state.direction}")
                logger.info(f"{thread_name}: Found cycle of length {cycle_length} at ({x}, {y})")
                
                return True
                
        visited[next_state] = step
        curr_state = next_state
    
    logger.debug(f"{thread_name}: No cycle found within {max_steps} steps at ({x}, {y})")
    
    return False

def solve_first(input_path: str) -> int:
    input_text = Path(input_path).read_text()
    grid, pos, direction = parse_input(input_text)
    visited = {pos}
    
    while True:
        next_pos = get_next_position(pos, direction)
        
        if (not is_inside_grid(next_pos, grid) or 
            grid[next_pos[1]][next_pos[0]] == '#'):
            direction = direction.turn_right()
            continue
            
        pos = next_pos
        visited.add(pos)
        
        if not is_inside_grid(get_next_position(pos, direction), grid):
            break
    
    return len(visited)

def solve_second(input_path: str) -> int:
    input_text = Path(input_path).read_text()
    grid, start_pos, start_dir = parse_input(input_text)
    height, width = len(grid), len(grid[0])
    debug = input_path.endswith('example.txt')
    
    positions = [
        (grid, (x, y), start_pos, start_dir, debug)
        for y in range(height)
        for x in range(width)
        if grid[y][x] == '.' and (x, y) != start_pos
    ]
    
    num_cores = os.cpu_count()
    logger.info(f"Checking {len(positions)} potential obstacle positions using {num_cores} CPU cores")
    
    with ProcessPoolExecutor(max_workers=num_cores) as executor:
        results = list(executor.map(check_position_creates_loop, positions))
    
    total_loops = sum(1 for r in results if r)
    logger.info(f"Found {total_loops} positions that create loops")

    return total_loops
