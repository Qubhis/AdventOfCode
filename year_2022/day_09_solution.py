from utils import load_file

INPUT_FILE = "year_2022/inputs/day_09.txt"

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

TAIL_POSSIBLE_ADJUSTMENTS = {
    (-1, 2): (-1, 1),
    (0, 2): (0, 1),
    (1, 2): (1, 1),
    (2, 1): (1, 1),
    (2, 0): (1, 0),
    (2, -1): (1, -1),
    (1, -2): (1, -1),
    (0, -2): (0, -1),
    (-1, -2): (-1, -1),
    (-2, -1): (-1, -1),
    (-2, 0): (-1, 0),
    (-2, 1): (-1, 1),
}


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class MapCoordinate(Coordinate):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.tail_visits = 1

    def tail_was_here(self):
        self.tail_visits += 1


class Rope:
    def __init__(self) -> None:
        self.head = Coordinate(0, 0)
        self.tail = Coordinate(0, 0)

    def move(self, direction: str):
        directions = {
            RIGHT: {"add_x": 1, "add_y": 0},
            LEFT: {"add_x": -1, "add_y": 0},
            UP: {"add_x": 0, "add_y": 1},
            DOWN: {"add_x": 0, "add_y": -1},
        }
        adjust_position = directions[direction]
        self.change_head_coordinates(adjust_position)

        return self.adjust_tail_coordinates()

    def change_head_coordinates(self, adjust_position: dict):
        self.head.x += adjust_position["add_x"]
        self.head.y += adjust_position["add_y"]

    def adjust_tail_coordinates(self):
        head_x, head_y = self.get_head_coordinates()
        tail_x, tail_y = self.get_tail_coordinates()
        diff_x, diff_y = (head_x - tail_x, head_y - tail_y)
        add_x, add_y = TAIL_POSSIBLE_ADJUSTMENTS.get((diff_x, diff_y), (0, 0))  # type: ignore

        self.tail.x += add_x
        self.tail.y += add_y
        has_moved = True if abs(add_x) > 0 or abs(add_y) > 0 else False

        return has_moved
        """
        Differences read top row, right column, bottom row, left column - clockwise (starting 11 hour)
        . . . . . . .
        . . H H H . .
        . H x x x H .
        . H x T x H .
        . H x x x H .
        . . H H H . .
        . . . . . . .

        """
        """
        x = -1, y = 2   =>  x = -1, y = 1
        x = 0, y = 2    =>  x = 0, y = 1
        x = 1, y = 2    =>  x = 1, y = 1

        x = 2, y = 1    =>  x = 1, y = 1
        x = 2, y = 0,   =>  x = 1, y = 0
        x = 2, y = -1   =>  x = 1, y = -1

        x = 1, y = -2   =>  x = 1, y = -1
        x = 0, y = -2   =>  x = 0, y = -1
        x = -1, y = -2  =>  x = -1, y = -1

        x = -2, y = -1, =>  x = -1, y = -1
        x = -2, y = 0,  =>  x = -1, y = 0
        x = -2, y = 1   =>  x = -1, y = 1
        """

    def get_head_coordinates(self):
        return (self.head.x, self.head.y)

    def get_tail_coordinates(self):
        return (self.tail.x, self.tail.y)


class MotionMapper:
    def __init__(self):
        self.rope = Rope()
        self.existing_coordinates = dict()
        self.add_new_coordinate(x=0, y=0)

    def process_move(self, direction: str, steps: int):
        for step in range(steps):
            has_tail_moved = self.rope.move(direction)
            if has_tail_moved:
                self.handle_tail_moved()

    def handle_tail_moved(self):
        (tail_x, tail_y) = self.rope.get_tail_coordinates()
        existing_coordinate = self.existing_coordinates.get((tail_x, tail_y), None)  # type: ignore
        if existing_coordinate:
            existing_coordinate.tail_was_here()
        else:
            self.add_new_coordinate(x=tail_x, y=tail_y)

    def add_new_coordinate(self, x, y):
        self.existing_coordinates[(x, y)] = MapCoordinate(x=x, y=y)


# ##########################################
motion_mapper = MotionMapper()
for line in load_file(INPUT_FILE):
    direction, steps = line.strip().split(" ")
    motion_mapper.process_move(direction, int(steps))

tail_visited_coordinates = [
    coordinate
    for coordinate in motion_mapper.existing_coordinates.values()
    if coordinate.tail_visits > 0
]

print(f"Tail visited {len(tail_visited_coordinates)} positions at least once.")
# print(f"The highest scenic score in our forest is {get_highest_scenic_score()}.")
