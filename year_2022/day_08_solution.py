from functools import reduce

from utils import load_file

INPUT_FILE = "year_2022/inputs/day_08.txt"
NORTH = "north"
EAST = "east"
SOUTH = "south"
WEST = "west"


class Tree:
    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height

    def to_dict(self):
        return {"row": self.row, "col": self.col, "height": self.height}


class Forest:
    def __init__(self, trees):
        self.width = 0
        self.height = 0
        self.trees = self.plant_trees(trees)
        self.determine_forest_size()

    def plant_trees(self, trees):
        planted_trees = []
        planting_row = []
        for row_idx, tree_row in enumerate(trees):
            for col_idx, tree_height in enumerate(tree_row):
                planting_row.append(Tree(row_idx, col_idx, int(tree_height)))
            planted_trees.append(planting_row.copy())
            planting_row.clear()

        return planted_trees

    def determine_forest_size(self):
        self.width = len(self.trees[0])
        self.height = len(self.trees)

    def get_tree_row_heights(self, row, start, end):
        return [tree.height for tree in self.trees[row][start:end]]

    def get_tree_col_heights(self, column, start, end):
        return [tree_row[column].height for tree_row in self.trees[start:end]]

    def is_tree_on_edge(self, tree):
        return (
            tree.row == 0
            or tree.row == self.height - 1
            or tree.col == 0
            or tree.col == self.width - 1
        )

    def is_tree_visible(self, tree, direction):
        if direction == WEST:
            max_height_from_direction = max(
                self.get_tree_row_heights(row=tree.row, start=0, end=tree.col)
            )

        elif direction == NORTH:
            max_height_from_direction = max(
                self.get_tree_col_heights(column=tree.col, start=0, end=tree.row)
            )

        elif direction == EAST:
            max_height_from_direction = max(
                self.get_tree_row_heights(row=tree.row, start=tree.col + 1, end=None)
            )

        elif direction == SOUTH:
            max_height_from_direction = max(
                self.get_tree_col_heights(column=tree.col, start=tree.row + 1, end=None)
            )
        else:
            max_height_from_direction = 9

        return tree.height > max_height_from_direction

    def get_visible_tree_count(self):
        tree_count = 2 * self.width + 2 * (self.height - 2)
        for tree_row in self.trees[1:-1]:
            for tree in tree_row[1:-1]:
                is_tree_visible = (
                    self.is_tree_visible(tree=tree, direction=WEST)
                    or self.is_tree_visible(tree=tree, direction=NORTH)
                    or self.is_tree_visible(tree=tree, direction=EAST)
                    or self.is_tree_visible(tree=tree, direction=SOUTH)
                )
                if is_tree_visible:
                    tree_count += 1

        return tree_count

    def calculate_scenic_score(self, tree):
        west_tree_heights = self.get_tree_row_heights(
            row=tree.row, start=0, end=tree.col
        )[::-1]
        north_tree_heights = self.get_tree_col_heights(
            column=tree.col, start=0, end=tree.row
        )[::-1]
        east_tree_heights = self.get_tree_row_heights(
            row=tree.row, start=tree.col + 1, end=None
        )
        south_tree_heights = self.get_tree_col_heights(
            column=tree.col, start=tree.row + 1, end=None
        )

        direction_heights = [
            west_tree_heights, north_tree_heights,
            east_tree_heights, south_tree_heights
        ]  # fmt: skip

        visible_trees_counts = []
        for tree_heights in direction_heights:
            visible_trees = 0
            for height in tree_heights:
                visible_trees += 1
                if height >= tree.height:
                    break

            visible_trees_counts.append(visible_trees)

        scenic_score = reduce((lambda a, b: a * b), visible_trees_counts)
        return scenic_score

    def get_tree_scenic_scores(self):
        scenic_scores = [
            self.calculate_scenic_score(tree)
            for tree_row in self.trees
            for tree in tree_row
        ]

        return scenic_scores


def get_total_visible_trees():
    forest = Forest(lines)
    return forest.get_visible_tree_count()


def get_highest_scenic_score():
    forest = Forest(lines)
    return max(forest.get_tree_scenic_scores())


# ##########################################
lines = [line.strip() for line in load_file(INPUT_FILE)]
print(f"You can spot {get_total_visible_trees()} trees from outside the grid.")
print(f"The highest scenic score in our forest is {get_highest_scenic_score()}.")
