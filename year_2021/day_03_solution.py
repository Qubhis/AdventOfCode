from collections import Counter

from utils import load_file


INPUT_FILE = "year_2021/day_03_input.txt"
ONE = "1"
ZERO = "0"


def transform_lines(lines: list):
    return [line.strip() for line in lines]


def get_most_common(iterable):
    counter = Counter(iterable)

    return counter.most_common()


def get_submarine_power_consumption():
    def convert_report(report: list[str]):
        len_line = len(report[0])
        converted_report = [""] * len_line
        for line in report:
            for idx, bit in enumerate(line):
                converted_report[idx] += bit

        return converted_report

    converted_report = convert_report(diagnostic_report)
    gamma_rate = ""
    epsilon_rate = ""

    for line in converted_report:
        most_common = get_most_common(line)
        gamma_rate += most_common[0][0]
        epsilon_rate += most_common[1][0]

    decimal_gamma_rate = int(gamma_rate, 2)
    decimal_epsilon_rate = int(epsilon_rate, 2)

    return decimal_gamma_rate * decimal_epsilon_rate


def get_co2_scrubber_rating():
    def get_most_common_bit_by_position(report, bit_position: int):
        bit_position_of_all_numbers = [number[bit_position] for number in report]

        return get_most_common(bit_position_of_all_numbers)

    def filter_oxygen_rating(report, bit_position: int):
        most_common = get_most_common_bit_by_position(report, bit_position)
        bit_to_keep = most_common[0][0]
        if most_common[0][1] == most_common[1][1]:
            bit_to_keep = "1"

        return list(filter(lambda number: number[bit_position] == bit_to_keep, report))

    def filter_scrubber_rating(report, bit_position: int):
        most_common = get_most_common_bit_by_position(report, bit_position)
        bit_to_keep = most_common[1][0]
        if most_common[0][1] == most_common[1][1]:
            bit_to_keep = "0"

        return list(filter(lambda number: number[bit_position] == bit_to_keep, report))

    def get_decimal_rating(report, filter_func):
        ratings = report.copy()
        rating_bit_position = 0
        while len(ratings) > 1:
            ratings = filter_func(ratings, rating_bit_position)
            rating_bit_position += 1

        return int(ratings[0], 2)

    # fmt: off
    decimal_oxygen_rating = get_decimal_rating(diagnostic_report, filter_oxygen_rating)
    decimal_scrubber_rating = get_decimal_rating(diagnostic_report, filter_scrubber_rating)
    # fmt: on

    return decimal_oxygen_rating * decimal_scrubber_rating


# ####################################
lines = load_file(INPUT_FILE)
diagnostic_report = transform_lines(lines)
print(
    f"What is the power consumption of the submarine: {get_submarine_power_consumption()}"
)
print(f"Life support rating of the submarine: {get_co2_scrubber_rating()}")
