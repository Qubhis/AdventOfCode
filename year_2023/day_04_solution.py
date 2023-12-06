import itertools
import math
import re
from collections import defaultdict
from functools import reduce

from utils import load_file


def remove_card_identifier(line):
    pattern = r"Card *\d+:"
    card_identifier = re.match(pattern, line).group()
    id_card = int(re.search(r"\d+", card_identifier).group())
    numbers = re.sub(pattern, "", line)
    return [id_card, numbers]


def parse_scratchcard_numbers(line_with_numbers):
    left, right = line_with_numbers.split("|")
    winning_nums = filter(lambda element: len(element) > 0, left.strip().split(" "))
    own_nums = filter(lambda element: len(element) > 0, right.strip().split(" "))
    return [list(winning_nums), list(own_nums)]


INPUT_FILE = "year_2023/inputs/day_04.txt"


def solution_1():
    lines = [line.replace("\n", "") for line in load_file(INPUT_FILE)]
    total_points = 0
    for card in lines:
        _, numbers = remove_card_identifier(card)
        winning_nums, my_nums = parse_scratchcard_numbers(numbers)
        number_of_matches = len(list(set(winning_nums) & set(my_nums)))
        if number_of_matches > 2:
            base = 2
            power = number_of_matches - 1
            total_points += base**power
        else:
            total_points += number_of_matches
    return total_points


def solution_2():
    lines = [line.replace("\n", "") for line in load_file(INPUT_FILE)]
    max_id_card = len(lines)
    cards_count = {card_number: 1 for card_number in range(1, max_id_card + 1)}
    for card in lines:
        id_card, numbers = remove_card_identifier(card)
        winning_nums, my_nums = parse_scratchcard_numbers(numbers)
        number_of_matches = len(list(set(winning_nums) & set(my_nums)))
        multiplier = cards_count.get(id_card, 1)
        for next_id_card in range(id_card + 1, id_card + number_of_matches + 1):
            if next_id_card > max_id_card:
                break
            cards_count[next_id_card] += 1 * multiplier

    total_scrathcards = sum([value for value in cards_count.values()])

    return total_scrathcards


print(f"The solution for the first task is: {solution_1()}")  # 21558
print(f"The solution for the second task is: {solution_2()}")
