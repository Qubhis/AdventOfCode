import string

from utils import load_file


INPUT_FILE = "year_2022/day_03_input.txt"
ascii_letters = list(string.ascii_lowercase + string.ascii_uppercase)
item_priority = {letter: value for value, letter in enumerate(ascii_letters, start=1)}


def get_priorities_sum_of_shared_item_type():
    rucksacks_contents = [line.strip() for line in lines]

    total_priorities_sum = 0
    for rucksack in rucksacks_contents:
        split_index = int(len(rucksack) * 0.5)
        first_compartment = set(rucksack[:split_index])
        second_compartment = set(rucksack[split_index:])

        for item in first_compartment:
            if item in second_compartment:
                total_priorities_sum += item_priority[item]
                break

    return total_priorities_sum


def get_priorities_sum_of_shared_group_item_type():
    elves_groups = []
    group_rucksacks = []
    for idx, rucksack in enumerate(rucksacks_contents, start=1):
        group_rucksacks.append(set(list(rucksack)))
        if idx % 3 == 0:
            elves_groups.append(group_rucksacks.copy())
            group_rucksacks = []

    total_priorities_sum = 0
    for group_rucksacks in elves_groups:
        for item in group_rucksacks[0]:
            if item in group_rucksacks[1] and item in group_rucksacks[2]:
                total_priorities_sum += item_priority[item]
                break

    return total_priorities_sum


# ############################################################3
lines = load_file(INPUT_FILE)
rucksacks_contents = [line.strip() for line in lines]
print(
    f"Priorities sum of shared item types: {get_priorities_sum_of_shared_item_type()}"
)
print(
    f"Priorities sum of shared group item types: {get_priorities_sum_of_shared_group_item_type()}"
)
