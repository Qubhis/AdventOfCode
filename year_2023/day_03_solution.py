import itertools
import math
import re
from collections import defaultdict

from utils import load_file

INPUT_FILE = "year_2023/inputs/day_03.txt"


def is_symbol(character):
    return character != "." and not character.isdigit()


# def solution_1():
#     # go line by line, character by character
#     # if is digit, store x and y ind
#     min_y = 0
#     max_y = len(lines) - 1
#     min_x = 0

#     engine_part_numbers = []

#     for y_index, line in enumerate(lines):
#         found_x_indexes = []
#         found_digits = []
#         max_x = len(line) - 1
#         for x_index, character in enumerate(line):
#             if character.isdigit():
#                 found_digits.append(character)
#                 found_x_indexes.append(x_index)
#                 if x_index != max_x:
#                     continue
#             if found_digits:
#                 adjacent_chars = ""
#                 # search for adjacent symbol, by getting adjacent characters and checking them for a symbol presence
#                 start_x = (
#                     found_x_indexes[0] - 1
#                     if found_x_indexes[0] != min_x
#                     else found_x_indexes[0]
#                 )
#                 end_x = (
#                     found_x_indexes[-1] + 2
#                     if found_x_indexes[-1] != max_x
#                     else found_x_indexes[-1] + 1
#                 )
#                 if y_index != min_y:
#                     adjacent_chars += lines[y_index - 1][start_x:end_x]
#                 adjacent_chars += lines[y_index][start_x:end_x]
#                 if y_index != max_y:
#                     adjacent_chars += lines[y_index + 1][start_x:end_x]
#                 if any(is_symbol(char) for char in adjacent_chars):
#                     engine_part_numbers.append(int("".join(found_digits)))
#                 # reset before next search up
#                 found_x_indexes = []
#                 found_digits = []

#     return sum(engine_part_numbers)


# def solution_2():
#     return ""


def get_symbols(lines):
    symbols = {
        (y_index, x_index)
        for y_index, line in enumerate(lines)
        for x_index, char in enumerate(line)
        if is_symbol(char)
    }

    return symbols


lines = [line.replace("\n", "") for line in load_file(INPUT_FILE)]
symbols = get_symbols(lines)
part_sum = 0
parts_by_symbol = defaultdict(list)
surrounding_offset = list(itertools.product((-1, 0, 1), (-1, 0, 1)))

for y_index, line in enumerate(lines):
    for match in re.finditer(r"\d+", line):
        number = int(match.group(0))
        boundary = {
            (y_index + y_offset, x_index + x_offset)
            for y_offset, x_offset in surrounding_offset
            for x_index in range(match.start(), match.end())
        }
        # find intersection of symbol and boundary of number
        if symbols & boundary:
            part_sum += number
        # find intersections and store number to the coordinates of a symbol
        for symbol in symbols & boundary:
            parts_by_symbol[symbol].append(number)


print(f"The solution for the first task is: {part_sum}")  # 525181
print(
    f"The solution for the second task is: {sum(math.prod(parts) for parts in parts_by_symbol.values() if len(parts) == 2)}"
)
