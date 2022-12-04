from utils import load_file


INPUT_FILE = "year_2022/inputs/day_04.txt"


def transform_lines(lines: list[str]):
    transformed_lines = []
    for line in lines:
        ranges = line.strip().split(",")
        transformed_line = []
        for single_range in ranges:
            [range_low, range_high] = single_range.split("-")
            transformed_line.append([int(range_low), int(range_high)])

        transformed_lines.append(transformed_line)

    return transformed_lines


def is_one_range_fully_included_in_another(range_pair):
    [[first_low, first_high], [second_low, second_high]] = range_pair

    return (first_low <= second_low and first_high >= second_high) or (
        second_low <= first_low and second_high >= first_high
    )


def does_one_range_overlap_with_another(range_pair):
    [[first_low, first_high], [second_low, second_high]] = range_pair

    return not (first_high < second_low or second_high < first_low)


def get_pair_count_fully_contained_range():
    range_pairs = transform_lines(lines)

    inclusive_pair_count = 0
    for range_pair in range_pairs:
        if is_one_range_fully_included_in_another(range_pair):
            inclusive_pair_count += 1

    return inclusive_pair_count


def get_overlapping_pair_count():
    range_pairs = transform_lines(lines)

    overlapping_pair_count = 0
    for range_pair in range_pairs:
        if is_one_range_fully_included_in_another(
            range_pair
        ) or does_one_range_overlap_with_another(range_pair):
            overlapping_pair_count += 1

    return overlapping_pair_count


# ##########################################
lines = load_file(INPUT_FILE)

print(
    f"Number of assignment pairs where one range fully contains the other: {get_pair_count_fully_contained_range()}"
)
print(
    f"Number of assignment pairs where one range overlaps with the other {get_overlapping_pair_count()}"
)
