from utils import load_file
import re
from functools import reduce


INPUT_FILE = "year_2023/inputs/day_02.txt"


def remove_game_identifier(game_record):
    pattern = r"Game \d+:"
    game_identifier = re.match(pattern, game_record).group()
    id_game = int(re.search(r"\d+", game_identifier).group())
    game_sets = re.sub(pattern, "", game_record)
    return [id_game, game_sets]


lines = [line.replace("\n", "") for line in load_file(INPUT_FILE)]


def solution_1():
    game_configuration = {"red": 12, "green": 13, "blue": 14}
    total_sum = 0
    for line in lines:
        valid_game = True
        id_game, game_sets = remove_game_identifier(line)
        cubes = game_sets.replace(";", ",").split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            if game_configuration[color] < int(count):
                valid_game = False
                break
        if valid_game:
            total_sum += id_game

    return total_sum


def solution_2():
    total_sum = 0
    for line in lines:
        minimum_set = {}
        _, game_sets = remove_game_identifier(line)
        cubes = game_sets.replace(";", ",").split(",")
        for cube in cubes:
            count, color = cube.strip().split(" ")
            current_color = minimum_set.get(color, None)
            if (
                current_color is not None and current_color <= int(count)
            ) or current_color is None:
                minimum_set[color] = int(count)
        numbers = list(minimum_set.values())
        game_power = reduce(lambda x, y: x * y, numbers)
        total_sum += game_power

    return total_sum


print(f"The solution for the first task is: {solution_1()}")
print(f"The solution for the second task is: {solution_2()}")
