import re

from input.day_7 import get_dummy_terminal_output, get_terminal_output

TOTAL_SPACE = 70000000
SPACE_REQUIRED = 30000000


def change_dir(new_dir: str, tree: dict, current_path: str) -> tuple[str, dict]:
    current_path = current_path + new_dir + "/"
    if current_path not in tree:
        tree[current_path] = int()
    return (current_path, tree)


if __name__ == "__main__":
    output = get_terminal_output()
    # output = get_dummy_terminal_output()

    tree = {"/": int()}
    current_path = "/"

    while len(output) != 0:
        current_line = output[0]
        output.remove(output[0])

        if current_line == "$ cd /":
            pass
        elif cd_match := re.search("^\\$ cd (?P<dir>\w+)$", current_line):
            change_to_dir = cd_match.groupdict().get("dir")
            current_path, tree = change_dir(change_to_dir, tree, current_path)
        elif current_line == "$ cd ..":
            current_path = re.sub("\\/\w+\\/$", "/", current_path)
        elif current_line == "$ ls":
            pass
        elif directory_match := re.search("^dir (?P<directory>\w+)$", current_line):
            directory = directory_match.groupdict().get("directory")
            directory_path = current_path + directory + "/"
            if directory_path not in tree:
                tree[directory_path] = int()
        elif file_match := re.search("^(?P<file_size>\d+) .+$", current_line):
            assert (
                current_path in tree
            ), f"Tree should already contain path ({current_path})"
            tree[current_path] += int(file_match.groupdict().get("file_size"))
        else:
            print(f"\n\n {current_line} \n\n")
            raise Exception("This case shouldn't happen", current_line)

    assert len(output) == 0, "Output should be empty"

    folder_sizes = {}

    for path in tree:
        dir_with_all_subdirs = {
            key: value for (key, value) in tree.items() if re.search(f"^{path}", key)
        }

        folder_sizes[path] = sum(dir_with_all_subdirs.values())

    # filter out folders whose size is above 100,000 and add up the rest
    small_size_folders = {
        key: value for (key, value) in folder_sizes.items() if value <= 100000
    }

    print(f"The answer for part 1 is {sum(small_size_folders.values())}")

    # --------

    space_available = TOTAL_SPACE - folder_sizes.get("/")
    space_needed = SPACE_REQUIRED - space_available

    folders_large_enough = {
        key: value for (key, value) in folder_sizes.items() if value >= space_needed
    }

    print(f"The answer for part 2 is {min(folders_large_enough.values())}")
