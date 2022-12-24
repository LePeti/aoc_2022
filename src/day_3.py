from string import ascii_lowercase

from input.day_3 import get_input_part_1, get_input_part_2


def get_upper_and_lower_case_abc() -> str:
    return ascii_lowercase + ascii_lowercase.upper()


def create_item_priorities() -> dict:
    items = get_upper_and_lower_case_abc()
    return {item: i + 1 for i, item in enumerate(items)}


def get_common_element(rucksack) -> str:
    compartment_len = int(len(rucksack) / 2)
    first_compartment = set(rucksack[0:compartment_len])
    second_compartment = set(rucksack[compartment_len:])
    common_element = first_compartment.intersection(second_compartment)

    return common_element.pop()


def get_common_element_from_group(r1: set, r2: set, r3: set) -> str:
    return r1.intersection(r2).intersection(r3).pop()


if __name__ == "__main__":

    rucksacks = get_input_part_1()

    all_common_elements = [get_common_element(rucksack) for rucksack in rucksacks]

    item_priorities = create_item_priorities()

    priorities_of_common_elements = [
        item_priorities.get(common_element) for common_element in all_common_elements
    ]

    print(f"part 1 answer: {sum(priorities_of_common_elements)}")

    # ---------

    rucksacks = get_input_part_2()

    rucksacks_grouped = [
        [rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]]
        for i in range(0, len(rucksacks), 3)
    ]

    common_elements_in_groups = [
        get_common_element_from_group(set(r1), set(r2), set(r3))
        for r1, r2, r3 in rucksacks_grouped
    ]

    priorities_of_common_elements = [
        item_priorities.get(common_element)
        for common_element in common_elements_in_groups
    ]

    print(f"part 2 answer: {sum(priorities_of_common_elements)}")
