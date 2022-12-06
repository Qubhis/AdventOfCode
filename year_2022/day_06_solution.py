from utils import load_file

INPUT_FILE = "year_2022/inputs/day_06.txt"


def get_character_count_prior_to_first_marker(unique_char_count):
    signal = lines[0].strip()
    for idx in range(unique_char_count, len(signal)):
        # fmt:off
        part_to_analyze = signal[idx - unique_char_count:idx]
        unique_chars = set([*part_to_analyze])
        if len(unique_chars) == unique_char_count:
            return idx


# ##########################################
lines = load_file(INPUT_FILE)
print(
    f"Processed characters before packet marker detected: {get_character_count_prior_to_first_marker(4)}"
)
print(
    f"Processed characters before message marker detected: {get_character_count_prior_to_first_marker(14)}"
)
