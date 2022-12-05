from collections import namedtuple
from utils import load_file


INPUT_FILE = "year_2022/inputs/day_05.txt"


def parse_crate_stacks(input_lines):
    horizontal_lines = []
    for line in input_lines[:-1]:
        array_line = []
        for idx in range(1, len(line), 4):
            crate_to_append = line[idx]
            if crate_to_append == " ":
                crate_to_append = ""
            array_line.append([crate_to_append])
        horizontal_lines.append(array_line[::-1])

    # transpose lines to columns (stacks)
    crane_stacks = [list() for _ in range(len(horizontal_lines[0]))]
    for line in horizontal_lines:
        for idx, stack in enumerate(line):
            if stack[0]:
                crane_stacks[idx].insert(0, stack)

    return crane_stacks[::-1]


def parse_rearrangement_steps(input_lines):
    Step = namedtuple("Step", ["crates_count", "origin", "destination"])
    parsed_steps = []
    for line in input_lines:
        parts = line.split(" ")
        parsed_steps.append(
            Step(
                crates_count=int(parts[1]),
                origin=int(parts[3]) - 1,
                destination=int(parts[5]) - 1,
            )
        )

    return parsed_steps


def transform_lines(lines):
    crate_stacks_input, rearrangement_steps_input = [], []
    for idx, line in enumerate(lines):
        # fmt: off
        if line == "\n":
            crate_stacks_input = lines[:idx]
            rearrangement_steps_input = lines[idx + 1:]
            break
            # fmt: on

    crate_stacks = parse_crate_stacks(crate_stacks_input)
    rearrangement_steps = parse_rearrangement_steps(rearrangement_steps_input)

    return crate_stacks, rearrangement_steps


def get_message_from_first_rearrangement():
    crate_stacks, rearrangement_steps = transform_lines(lines)
    for step in rearrangement_steps:
        for _ in range(step.crates_count):
            stack = crate_stacks[step.origin].pop()
            crate_stacks[step.destination].append(stack)

    return "".join([stack[-1][0] for stack in crate_stacks])


def get_message_from_second_rearrangement():
    crate_stacks, rearrangement_steps = transform_lines(lines)
    for step in rearrangement_steps:
        for idx in range(step.crates_count):
            stack = crate_stacks[step.origin].pop()
            if idx == 0:
                crate_stacks[step.destination].append(stack)
            else:
                crate_stacks[step.destination].insert(-idx, stack)

    return "".join([stack[-1][0] for stack in crate_stacks])


# ##########################################
lines = load_file(INPUT_FILE)
print(
    f"The message after the first rearrangement is: {get_message_from_first_rearrangement()}"
)
print(
    f"The message after the second rearrangement is: {get_message_from_second_rearrangement()}"
)
