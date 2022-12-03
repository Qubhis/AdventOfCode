from utils import load_file


INPUT_FILE = "year_2021/day_01_input.txt"


def transform_lines(lines: list):
    return [int(line.strip()) for line in lines]


def get_total_increases(measurements: list) -> int:
    total_increases = 0
    for idx, measurement in enumerate(measurements):
        if idx == 0:
            continue

        if measurement > measurements[idx - 1]:
            total_increases += 1

    return total_increases


def get_number_of_depth_measurement_increases():
    measurements = transform_lines(lines)

    return get_total_increases(measurements)


def get_number_of_three_measurement_increases():
    measurements = transform_lines(lines)
    three_dimensional_sums = []
    for idx, measurement in enumerate(measurements):
        if idx + 2 > len(measurements) - 1:
            # last index already counted in previous sum
            break

        three_dimensional_sums.append(
            measurement + measurements[idx + 1] + measurements[idx + 2]
        )

    return get_total_increases(three_dimensional_sums)


# ####################################
lines = load_file(INPUT_FILE)
print(
    f"The number of times a depth measurement increases: {get_number_of_depth_measurement_increases()}"
)
print(
    f"The number of times a 'three-measurement' increases: {get_number_of_three_measurement_increases()}"
)
