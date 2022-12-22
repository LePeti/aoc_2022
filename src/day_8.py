import numpy as np
from input.day_8 import get_map


def count_visible_trees(woods) -> int:
    visible_outer = woods.shape[0] * 2 + (woods.shape[1] - 2) * 2
    visible_inner = 0

    for i in range(1, woods.shape[0] - 1):
        for j in range(1, woods.shape[1] - 1):
            if is_tree_visible(i, j, woods[i, j], woods):
                visible_inner += 1

    return visible_outer + visible_inner


def is_tree_visible(i: int, j: int, height: int, map: np.ndarray) -> bool:
    trees_above = map[:i, j]
    trees_below = map[i + 1:, j]
    trees_left = map[i, :j]
    trees_right = map[i, j + 1:]

    return (
        int(all(trees_above < height)) or
        int(all(trees_below < height)) or
        int(all(trees_left < height)) or
        int(all(trees_right < height))
    )


if __name__ == "__main__":
    map = get_map()

    visible_trees = count_visible_trees(map)

    print(f"Part 1 answer is {visible_trees}")
