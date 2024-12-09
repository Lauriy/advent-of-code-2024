def solve_first(file_path: str) -> int:
    with open(file_path) as f:
        grid = [line.strip() for line in f]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols

    def check_direction(x: int, y: int, dx: int, dy: int) -> bool:
        word = ""
        for i in range(4):
            new_x, new_y = x + i * dx, y + i * dy
            if not is_valid(new_x, new_y):
                return False
            word += grid[new_x][new_y]
        return word == "XMAS"

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1

    return count


def solve_second(file_path: str) -> int:
    with open(file_path) as f:
        grid = [line.strip() for line in f]
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols

    def check_mas(x: int, y: int, dx: int, dy: int) -> bool:
        word = ""
        for i in range(3):
            new_x, new_y = x + i * dx, y + i * dy
            if not is_valid(new_x, new_y):
                return False
            word += grid[new_x][new_y]
        return word in ["MAS", "SAM"]

    # Check for X-shaped patterns
    for i in range(rows - 2):
        for j in range(1, cols - 1):
            if check_mas(i, j - 1, 1, 1) and check_mas(i, j + 1, 1, -1):
                count += 1

    return count
