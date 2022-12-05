from utils import load_file


INPUT_FILE = "year_2021/inputs/day_04.txt"

POSITION = "position"
ROW = "row"
COLUMN = "column"
IS_MARKED = "is_marked"


class BingoBoard:
    def __init__(self, board_rows) -> None:
        self.board_rows = board_rows.copy()
        self.numbers_information = self.populate_numbers()

    def populate_numbers(self):
        numbers_information = {}
        for row_idx, row_numbers in enumerate(self.board_rows):
            for column_idx, number in enumerate(row_numbers):
                numbers_information[number] = {
                    POSITION: {ROW: row_idx, COLUMN: column_idx},
                    IS_MARKED: False,
                }

        return numbers_information

    def mark_drawn_number_if_exist(self, drawn_number):
        number_position = self.numbers_information.get(drawn_number, None)
        if number_position and not number_position[IS_MARKED]:
            number_position[IS_MARKED] = True
            return True
        else:
            return False

    def has_won(self, drawn_number):
        number_position = self.numbers_information[drawn_number][POSITION]
        row = self.board_rows[number_position[ROW]]
        row_marked_states = [
            self.numbers_information[number][IS_MARKED] for number in row
        ]
        are_all_nums_in_row_marked = all(row_marked_states)
        if are_all_nums_in_row_marked:
            return True

        column_marked_states = []
        for row in self.board_rows:
            number = row[number_position[COLUMN]]
            column_marked_states.append(self.numbers_information[number][IS_MARKED])
        are_all_nums_in_column_marked = all(column_marked_states)
        if are_all_nums_in_column_marked:
            return True

        return False

    def get_all_unmarked_numbers(self):
        unmarked_numbers = [
            int(number)
            for number, information in self.numbers_information.items()
            if information[IS_MARKED] is False
        ]
        return unmarked_numbers

    def calculate_final_score(self, last_drawn_number):
        unmarked_numbers = self.get_all_unmarked_numbers()

        return sum(unmarked_numbers) * int(last_drawn_number)


def extract_play_data(lines):
    drawn_numbers = [number for number in lines[0].strip().split(",")]
    bingo_boards = []
    board_numbers = []
    for line in lines[2:]:
        if line == "\n":
            bingo_boards.append(BingoBoard(board_numbers))
            board_numbers = []
            continue

        # fmt: off
        numbers = [
            line[split_idx - 2: split_idx].strip()  # fmt: on
            for split_idx in range(2, len(line), 3)
        ]
        board_numbers.append(numbers)
    else:
        bingo_boards.append(BingoBoard(board_numbers))

    return drawn_numbers, bingo_boards


def get_winning_bingo_board_score():
    drawn_numbers, bingo_boards = extract_play_data(lines)
    for number in drawn_numbers:
        for board in bingo_boards:
            if board.mark_drawn_number_if_exist(number) and board.has_won(number):

                return board.calculate_final_score(number)


def pop_boards(bingo_boards, boards_to_pop):
    for popped_board in boards_to_pop:
        pop_idx = bingo_boards.index(popped_board)
        bingo_boards.pop(pop_idx)


def get_last_winning_bingo_board_score():
    drawn_numbers, bingo_boards = extract_play_data(lines)

    for number in drawn_numbers:
        boards_to_pop = []
        for idx in range(0, len(bingo_boards)):
            board = bingo_boards[idx]
            if board.mark_drawn_number_if_exist(number) and board.has_won(number):
                boards_to_pop.append(board)

        if len(bingo_boards) == len(boards_to_pop):
            return boards_to_pop[-1].calculate_final_score(number)
        else:
            pop_boards(bingo_boards, boards_to_pop)


# ####################################
lines = load_file(INPUT_FILE)
print(f"Final score of winning bingo board: {get_winning_bingo_board_score()}")
print(
    f"Final score of the last winning bingo board: {get_last_winning_bingo_board_score()}"
)
