from input.day_6 import get_input


def are_4_letters_unique(letters: str) -> bool:
    assert len(letters) == 4, (
        "input must be 4 letters, e.g. 'abcd'. "
        f"Your input was '{letters}' (length of {len(letters)})"
    )
    return len(set(letters)) == 4


if __name__ == "__main__":
    signal = get_input()

    i = 0

    while not are_4_letters_unique(signal[i:i + 4]):
        i += 1

    print(f"Answer for part 1 is {i + 4}")
