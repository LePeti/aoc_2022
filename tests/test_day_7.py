from src.day_7 import change_dir


class TestPartOne:
    def test_changeDir_returns_updated_tree_and_correct_path(self):
        current_path, tree = change_dir(new_dir="foo", tree={"/": int()}, current_path="/")
        assert current_path == "/foo/"
        assert tree == {"/": int(), "/foo/": int()}
