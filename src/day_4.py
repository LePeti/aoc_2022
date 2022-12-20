from input.day_4 import get_input_part_1


def do_sections_overlap(s1: tuple, s2: tuple) -> bool:
    s11 = set(range(s1[0], s1[1] + 1))
    s22 = set(range(s2[0], s2[1] + 1))
    intersect = s11.intersection(s22)

    return (intersect == s11) or (intersect == s22)


if __name__ == "__main__":
    elf_pairs = get_input_part_1()

    overlapping_pairs = [int(do_sections_overlap(*elf_pair)) for elf_pair in elf_pairs]

    print(f"answer for part 1: {sum(overlapping_pairs)}")

# --------
