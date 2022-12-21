from src.day_7 import change_dir


class TestPartOne:
    def test_changeDir_returns_updated_tree_and_correct_path(self):
        path, tree = change_dir(new_dir="foo", tree={"/": []}, path=["/"])
        assert path == ["/", "foo"]
        assert tree == {"/": [{"foo": []}]}
