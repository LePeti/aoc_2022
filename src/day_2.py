from input.day_2 import get_input


def rps_round(opponents_move, your_move) -> int:
    if opponents_move == "A":
        if your_move == "X":
            return 4
        if your_move == "Y":
            return 8
        if your_move == "Z":
            return 3
    if opponents_move == "B":
        if your_move == "X":
            return 1
        if your_move == "Y":
            return 5
        if your_move == "Z":
            return 9
    if opponents_move == "C":
        if your_move == "X":
            return 7
        if your_move == "Y":
            return 2
        if your_move == "Z":
            return 6


def strategy_to_move(opponents_move, your_strategy) -> str:
    if opponents_move == "A":
        if your_strategy == "X":
            return "Z"
        if your_strategy == "Y":
            return "X"
        if your_strategy == "Z":
            return "Y"
    if opponents_move == "B":
        if your_strategy == "X":
            return "X"
        if your_strategy == "Y":
            return "Y"
        if your_strategy == "Z":
            return "Z"
    if opponents_move == "C":
        if your_strategy == "X":
            return "Y"
        if your_strategy == "Y":
            return "Z"
        if your_strategy == "Z":
            return "X"


if __name__ == "__main__":

    input = get_input()

    results = [rps_round(*round) for round in input]

    print(f"part 1 answer: {sum(results)}")

    input_with_moves = [
        (opponents_move, strategy_to_move(opponents_move, your_strategy))
        for opponents_move, your_strategy in input
    ]

    part_2_results = [rps_round(*round) for round in input_with_moves]

    print(f"part 2 answer: {sum(part_2_results)}")
