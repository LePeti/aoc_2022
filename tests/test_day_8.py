from src.day_8 import count_visible_trees
from input.day_8 import get_dummy_map

import numpy as np

dummy_map = get_dummy_map()


class TestPartOne:
    def test_count_visible_trees_given_5by5_map(self):
        assert count_visible_trees(get_dummy_map()) == 23
