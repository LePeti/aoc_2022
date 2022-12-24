from src.day_9 import tail_follows_head


class TestPartOne:
    def test_given_max_dist_1_no_move(self):
        assert tail_follows_head((0, 0), (0, 1), "D") == (0, 1)
        assert tail_follows_head((0, 0), (0, 1), "R") == (0, 1)

        assert tail_follows_head((0, 0), (1, 0), "L") == (1, 0)
        assert tail_follows_head((0, 0), (1, 0), "U") == (1, 0)

        assert tail_follows_head((1, 1), (0, 0), "U") == (0, 0)
        assert tail_follows_head((1, 1), (0, 0), "L") == (0, 0)

    def test_given_dist_2_move_straight(self):
        assert tail_follows_head((0, 0), (2, 0), "U") == (1, 0)
        assert tail_follows_head((2, 0), (0, 0), "D") == (1, 0)
        assert tail_follows_head((1, 0), (1, 2), "L") == (1, 1)
        assert tail_follows_head((1, 2), (1, 0), "R") == (1, 1)

    def test_given_dist_2_and_1_move_diagonally(self):
        assert tail_follows_head((0, 0), (2, 1), "U") == (1, 0)
        assert tail_follows_head((0, 2), (2, 1), "D") == (1, 2)
        assert tail_follows_head((2, 0), (0, 1), "L") == (1, 0)
        assert tail_follows_head((2, 2), (0, 1), "R") == (1, 2)
