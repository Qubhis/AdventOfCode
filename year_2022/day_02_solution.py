from utils import load_file


INPUT_FILE = "year_2022/day_02_input.txt"

LOST = "lost"
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
DRAW = "draw"
WIN = "win"

scores = {
    LOST: 0,
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
    DRAW: 3,
    WIN: 6,
}

options_mapping = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}


def calculate_score_part_1():
    combinations = {
        "A X": DRAW,
        "A Y": WIN,
        "A Z": LOST,
        "B X": LOST,
        "B Y": DRAW,
        "B Z": WIN,
        "C X": WIN,
        "C Y": LOST,
        "C Z": DRAW,
    }

    total_score = 0
    for combination in rounds:
        score_for_round = scores[combinations[combination]]
        score_for_choice = scores[options_mapping[combination[-1]]]
        total_score += score_for_choice + score_for_round

    return total_score


def calculate_score_part_2():
    combinations_2 = {
        "A X": [SCISSORS, LOST],
        "A Y": [ROCK, DRAW],
        "A Z": [PAPER, WIN],
        "B X": [ROCK, LOST],
        "B Y": [PAPER, DRAW],
        "B Z": [SCISSORS, WIN],
        "C X": [PAPER, LOST],
        "C Y": [SCISSORS, DRAW],
        "C Z": [ROCK, WIN],
    }

    total_score_2 = 0
    for combination in rounds:
        expected_round = combinations_2[combination]
        score_for_choice = scores[expected_round[0]]
        score_for_round = scores[expected_round[1]]
        total_score_2 += score_for_choice + score_for_round

    return total_score_2


# #################################
lines = load_file(INPUT_FILE)
rounds = [line.strip() for line in lines]

print(f"Score count when x, y, z is rock, paper, scissors:  {calculate_score_part_1()}")
print(
    f"Score count when x, y, z is expected outcome of the round: {calculate_score_part_2()}"
)
