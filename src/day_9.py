import numpy as np

from input.day_9 import get_instructions


def tail_follows_head(
    head_pos: tuple[int, int], tail_pos: tuple[int, int], last_head_move: str
) -> tuple[int, int]:
    head_i, head_j = head_pos
    tail_i, tail_j = tail_pos

    i_dist = abs(head_i - tail_i)
    j_dist = abs(head_j - tail_j)

    if max(i_dist, j_dist) <= 1:
        return tail_pos  # no move
    elif ((i_dist == 2) & (j_dist == 0)) | ((i_dist == 0) & (j_dist == 2)):
        return move_in_direction(tail_pos, last_head_move)
    elif ((i_dist == 2) & (j_dist == 1)) | ((i_dist == 1) & (j_dist == 2)):
        return tail_follows_head_diagonally(head_pos, tail_pos)
    else:
        raise Exception("This case should not exist.", head_pos, tail_pos)


def move_in_direction(
    current_position: tuple[int, int], direction: str
) -> tuple[int, int]:
    i, j = current_position
    if direction == "D":
        return (i + 1, j)
    elif direction == "U":
        return (i - 1, j)
    elif direction == "L":
        return (i, j - 1)
    elif direction == "R":
        return (i, j + 1)
    else:
        raise Exception("This case shouldn't happen", direction)


def tail_follows_head_diagonally(
    head_pos: tuple[int, int], tail_pos: tuple[int, int]
) -> tuple[int, int]:
    head_i, head_j = head_pos
    tail_i, tail_j = tail_pos

    if tail_i < head_i:
        new_tail_i = tail_i + 1
    else:
        new_tail_i = tail_i - 1

    if tail_j < head_j:
        new_tail_j = tail_j + 1
    else:
        new_tail_j = tail_j - 1

    return (new_tail_i, new_tail_j)


if __name__ == "__main__":
    input = get_instructions()
    total_direction = sum([instruction[1] for instruction in input])

    grid = np.zeros([5001, 5001])
    head_position = (2501, 2501)
    tail_position = (2501, 2501)

    grid[tail_position] = 1

    for direction, num_steps in input:
        for step in range(num_steps):
            head_position = move_in_direction(head_position, direction)
            tail_position = tail_follows_head(head_position, tail_position, direction)
            grid[tail_position] += 1

    print(f"The naswer for part 1 is {(grid > 0).sum()}")

    # ----------
