import numpy as np

from input.day_8 import get_map


def count_visible_trees(map: np.ndarray) -> int:
    visible_outer = map.shape[0] * 2 + (map.shape[1] - 2) * 2
    visible_inner = 0

    for i in range(1, map.shape[0] - 1):
        for j in range(1, map.shape[1] - 1):
            if is_tree_visible(i, j, map):
                visible_inner += 1

    return visible_outer + visible_inner


def highest_scenic_score(map: np.ndarray) -> tuple[int, int, int]:
    highest_score = 0
    i_high = 0
    j_high = 0

    for i in range(1, map.shape[0]):
        for j in range(1, map.shape[1]):
            current_score = get_tree_scenic_score(i, j, map)
            if current_score > highest_score:
                highest_score = current_score
                i_high = i
                j_high = j

    return highest_score, i_high, j_high


def is_tree_visible(i: int, j: int, map: np.ndarray) -> bool:
    trees_above = map[:i, j]
    trees_below = map[i + 1 :, j]
    trees_left = map[i, :j]
    trees_right = map[i, j + 1 :]

    tree_height = map[i, j]

    return (
        int(all(trees_above < tree_height))
        or int(all(trees_below < tree_height))
        or int(all(trees_left < tree_height))
        or int(all(trees_right < tree_height))
    )


def get_tree_scenic_score(i: int, j: int, map: np.ndarray) -> int:
    scenic_score = 1

    trees_above = np.flip(map[:i, j])
    trees_below = map[i + 1 :, j]
    trees_left = np.flip(map[i, :j])
    trees_right = map[i, j + 1 :]

    tree_height = map[i, j]

    scenic_score *= find_view_blocking_tree_distance(tree_height, trees_above)
    scenic_score *= find_view_blocking_tree_distance(tree_height, trees_below)
    scenic_score *= find_view_blocking_tree_distance(tree_height, trees_left)
    scenic_score *= find_view_blocking_tree_distance(tree_height, trees_right)

    return scenic_score


def find_view_blocking_tree_distance(
    current_tree_height: int, tree_heights: np.ndarray
) -> int:
    try:
        distance = np.where(tree_heights >= current_tree_height)[0][0] + 1
    except IndexError:
        distance = len(tree_heights)
    return distance


if __name__ == "__main__":
    map = get_map()

    visible_trees = count_visible_trees(map)

    print(f"Part 1 answer is {visible_trees}")

    # -------

    score, i, j = highest_scenic_score(map)

    print(f"Part 2 answer is {score} ({i}, {j})")
