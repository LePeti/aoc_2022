from input.day_7 import get_terminal_output
import re


def change_dir(new_dir: str, tree: dict, path: list) -> tuple[str, dict]:
    tree[path[-1]].append({new_dir: []})
    path.append(new_dir)
    return (path, tree)


if __name__ == "__main__":
    output = get_terminal_output()

    tree = {"/": []}
    path = ["/"]

    while len(output) != 0:
        current_line = output[0]
        output.remove(output[0])

        if current_line == "$ cd /":
            pass
        elif match := re.search("^\\$ cd (?P<dir>\w+)$", current_line):
            change_to_dir = match.groupdict().get("dir")
            path, tree = change_dir(change_to_dir, tree, path)
        elif current_line == "$ cd ..":
            path.pop()
        elif current_line == "$ ls":
            pass
        else:
            print(f"\n\n {current_line} \n\n")
            raise Exception("This case shouldn't happen", current_line)
