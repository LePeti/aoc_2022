from input.day_6 import get_input


def are_n_letters_unique(letters: str, n: int) -> bool:
    assert len(letters) == n, (
        f"input must be {n} letters. Your input was '{letters}' (length of {len(letters)})"
    )
    return len(set(letters)) == n


if __name__ == "__main__":
    signal = get_input()

    i = 0

    while not are_n_letters_unique(signal[i:i + 4], 4):
        i += 1

    print(f"Answer for part 1 is {i + 4}")

# -----------

    i = 0

    while not are_n_letters_unique(signal[i:i + 14], 14):
        i += 1

    print(f"Answer for part 1 is {i + 14}")
