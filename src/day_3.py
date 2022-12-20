from input.day_3 import get_input
from string import ascii_lowercase


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


if __name__ == "__main__":

    rucksacks = get_input()

    all_common_elements = [get_common_element(rucksack) for rucksack in rucksacks]

    item_priorities = create_item_priorities()

    priorities_of_common_elements = [
        item_priorities.get(common_element) for common_element in all_common_elements
    ]

    print(f"part 1 answer: {sum(priorities_of_common_elements)}")
