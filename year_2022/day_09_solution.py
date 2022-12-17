from dataclasses import dataclass

from utils import load_file

INPUT_FILE = "year_2022/inputs/day_09.txt"

RIGHT = "R"
LEFT = "L"
UP = "U"
DOWN = "D"

DIRECTIONS = {
    RIGHT: {"add_x": 1, "add_y": 0},
    LEFT: {"add_x": -1, "add_y": 0},
    UP: {"add_x": 0, "add_y": 1},
    DOWN: {"add_x": 0, "add_y": -1},
}


@dataclass
class Knot:
    x: int
    y: int

    def change_position(self, add_x, add_y):
        self.x += add_x
        self.y += add_y


class Rope:
    def __init__(self, knots_count):
        self.knots = self.create_rope(knots_count)

    def create_rope(self, knots_count):
        return [Knot(x=0, y=0) for _ in range(knots_count)]

    def __len__(self):
        return len(self.knots)

    def get_head(self):
        return self.knots[0]

    def get_knot_and_previous(self, knot_idx):
        return self.knots[knot_idx], self.knots[knot_idx - 1]

    def get_tail(self):
        return self.knots[-1]


def get_tail_visits_for_rope(knots_count):
    visited_positions = set()
    rope = Rope(knots_count)

    for (direction, distance) in lines:
        for _ in range(int(distance)):
            # Move the head
            head = rope.get_head()
            head.change_position(**DIRECTIONS[direction])
            # Move other knots
            for knot_idx in range(1, len(rope)):
                curr_knot, previous_knot = rope.get_knot_and_previous(knot_idx)

                delta_x, delta_y = (
                    previous_knot.x - curr_knot.x,
                    previous_knot.y - curr_knot.y,
                )

                # If the knot is further than 1 away from the previous knot, move it closer
                if delta_x >= 2 or delta_x <= -2 or delta_y >= 2 or delta_y <= -2:
                    add_x = max(-1, min(1, delta_x))
                    add_y = max(-1, min(1, delta_y))

                    curr_knot.change_position(add_x=add_x, add_y=add_y)

                tail = rope.get_tail()
                visited_positions.add((tail.x, tail.y))

    return len(visited_positions)


# #################################################################3
lines = [line.strip().split(" ") for line in load_file(INPUT_FILE)]
print(
    f"Tail visited {get_tail_visits_for_rope(knots_count=2)} positions at least once."
)
print(
    f"Tail visited {get_tail_visits_for_rope(knots_count=10)} positions at least once."
)
