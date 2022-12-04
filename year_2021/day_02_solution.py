from utils import load_file


INPUT_FILE = "year_2021/inputs/day_02.txt"
FORWARD = "forward"
UP = "up"


class SubmarinePosition:
    def __init__(self, is_aimed=False):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0
        self.is_aimed = is_aimed

    def handle_step_forward(self, value):
        if self.is_aimed:
            self.depth += self.aim * value

        self.horizontal_position += value

    def handle_step_up(self, value):
        if self.is_aimed:
            self.aim -= value
        else:
            self.depth -= value

    def handle_step_down(self, value):
        if self.is_aimed:
            self.aim += value
        else:
            self.depth += value

    def get_product_of_horizontal_position_and_depth(self):
        return self.horizontal_position * self.depth


def transform_lines(lines: list):
    transform_lines = []
    for line in lines:
        columns = line.split(" ")
        transform_lines.append([columns[0], int(columns[1])])

    return transform_lines


def calculate_submarine_position(is_aimed=False):
    submarine_position = SubmarinePosition(is_aimed)

    for step, value in navigation_steps:
        if step == FORWARD:
            submarine_position.handle_step_forward(value)
        elif step == UP:
            submarine_position.handle_step_up(value)
        else:
            submarine_position.handle_step_down(value)

    return submarine_position.get_product_of_horizontal_position_and_depth()


# ####################################
lines = load_file(INPUT_FILE)
navigation_steps = transform_lines(lines)
print(f"Product of final submarine position: {calculate_submarine_position()}")
print(
    f"Product of final aimed submarine position: {calculate_submarine_position(is_aimed=True)}"
)
