from input.day_5 import get_moves_input, get_crates_input


def move_crates(crates: list[list], number: int, fro: int, to: int) -> list[list]:
    for i in range(number):
        crates[to - 1].append(crates[fro - 1].pop())

    return crates


if __name__ == "__main__":
    crates = get_crates_input()
    moves = get_moves_input()

    # this way, the crate on top of each stack is the last element of the list
    for crate in crates:
        crate.reverse()

# move 10 from 6 to 3
for move in moves:
    crates = move_crates(crates, *move)

top_crates = [stack[-1] for stack in crates]

print(f"Part 1 answer is {''.join(top_crates)}")
