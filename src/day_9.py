from pathlib import Path


def solve_first(input_path: str) -> int:
    disk_map = Path(input_path).read_text().strip()

    blocks = []
    file_id = 0
    is_free_space = False

    for char in disk_map:
        if is_free_space:
            blocks.extend([-1] * int(char))  # -1 is free
        else:
            blocks.extend([file_id] * int(char))
            file_id += 1
        is_free_space = not is_free_space

    checksum = 0
    left = 0
    right = len(blocks) - 1

    while left <= right:
        if blocks[left] == -1:
            while right > left and blocks[right] == -1:
                right -= 1
            if right > left:
                checksum += left * blocks[right]
                right -= 1
        else:
            checksum += left * blocks[left]
        left += 1

    return checksum


def solve_second(input_path: str) -> int:
    disk_map = Path(input_path).read_text().strip()

    blocks = []
    file_sizes = {}
    file_id = 0
    is_free_space = False

    for char in disk_map:
        size = int(char)
        if is_free_space:
            blocks.extend([-1] * size)
        else:
            blocks.extend([file_id] * size)
            file_sizes[file_id] = size
            file_id += 1
        is_free_space = not is_free_space  # toggle

    # reverse order (highest ID first)
    for current_file in range(file_id - 1, -1, -1):
        file_size = file_sizes[current_file]

        file_start = -1
        for i, block in enumerate(blocks):
            if block == current_file:
                file_start = i
                break

        free_start = -1
        free_count = 0
        for i, block in enumerate(blocks):
            if i >= file_start:  # can't move
                break
            if block == -1:
                if free_count == 0:
                    free_start = i
                free_count += 1
            else:
                free_start = -1
                free_count = 0

            if free_count == file_size:
                # move
                for j in range(file_size):
                    blocks[free_start + j] = current_file
                # clear
                for j in range(file_size):
                    blocks[file_start + j] = -1
                break

    checksum = 0
    for i, block in enumerate(blocks):
        if block == -1:
            continue
        checksum += i * block

    return checksum
