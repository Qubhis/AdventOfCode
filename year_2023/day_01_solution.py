from utils import load_file
import re


INPUT_FILE = "year_2023/inputs/day_01.txt"

calibration_document_lines = [line.replace("\n", "") for line in load_file(INPUT_FILE)]


def solution_1():
    calibration_values = []
    for document_line in calibration_document_lines:
        # 1. remove all non digit characters
        only_digits_line = "".join(
            character for character in document_line if character.isdigit()
        )
        # 2. take first and the last digit and make a 2-digit number'
        value = int(f"{only_digits_line[0]}{only_digits_line[-1]}")
        # 3. append to calibration values
        calibration_values.append(value)

    # 4. finally sum all calibration values
    sum_of_all_calibration_values = sum(calibration_values)

    return sum_of_all_calibration_values


def solution_2():
    calibration_values = []
    for document_line in calibration_document_lines:
        word_replacements = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4r",
            "five": "f5e",
            "six": "s6x",
            "seven": "s7n",
            "eight": "e8t",
            "nine": "n9e",
        }
        # 1. substitute all digit words with digits
        translated_line = document_line
        for word, digit in word_replacements.items():
            translated_line = translated_line.replace(word, digit)
        # 2. remove all non digit characters
        only_digits_line = "".join(
            character for character in translated_line if character.isdigit()
        )
        # 3. take first and the last digit and make a 2-digit number'
        value = int(f"{only_digits_line[0]}{only_digits_line[-1]}")
        # 4. append to calibration values
        calibration_values.append(value)

    # 4. finally sum all calibration values
    sum_of_all_calibration_values = sum(calibration_values)

    return sum_of_all_calibration_values


print(f"The sum of all calibration values is: {solution_1()}")  # 54632
print(f"The sum of all calibration values is: {solution_2()}")  # 54019
