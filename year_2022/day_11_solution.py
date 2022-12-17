import math

from utils import load_file


INPUT_FILE = "year_2022/inputs/day_11.txt"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


class Monkey:
    def __init__(self, **kwargs) -> None:
        self.items: list[int] = kwargs["items"]
        self.operation = kwargs["operation"]
        self.operand = (
            int(kwargs["operand"]) if kwargs["operand"].isnumeric() else "self"
        )
        self.division_test = kwargs["division_test"]
        self.total_inspected_items = 0

    def operate_on_worriness(self, worry_level):
        operand = worry_level if self.operand == "self" else self.operand

        return OPERATIONS[self.operation](worry_level, operand)

    def get_bored(self, worry_level):
        return math.floor(worry_level / 3)

    def get_catching_monkey_index(self, worry_level):
        is_divisible = worry_level % self.division_test["by"] == 0

        return (
            self.division_test["if_true"]
            if is_divisible
            else self.division_test["if_false"]
        )

    def inspect_items(self, get_bored=True):
        inspected_items = []
        while len(self.items):
            item = self.remove_item()
            worry_level = self.operate_on_worriness(item)
            if get_bored:
                worry_level = self.get_bored(worry_level)
            catching_monkey_idx = self.get_catching_monkey_index(worry_level)
            inspected_items.append((worry_level, catching_monkey_idx))

        self.total_inspected_items += len(inspected_items)

        return inspected_items

    def remove_item(self):
        return self.items.pop()

    def add_item(self, item):
        self.items.append(item)


def parse_input_get_monkeys():
    ROW_SIZE = 7
    lines = [line.strip() for line in load_file(INPUT_FILE)]

    monkeys = []
    for idx in range(0, len(lines), ROW_SIZE):
        items = parse_starting_items(lines[idx + 1])
        operation, operand = parse_operation(lines[idx + 2])
        divisible_by = parse_test(lines[idx + 3])
        if_true = parse_if_branch(lines[idx + 4])
        if_false = parse_if_branch(lines[idx + 5])
        monkey_properties = {
            "items": items,
            "operation": operation,
            "operand": operand,
            "division_test": {
                "by": divisible_by,
                "if_true": if_true,
                "if_false": if_false,
            },
        }

        monkeys.append(Monkey(**monkey_properties))

    return monkeys


def parse_starting_items(line):
    _, string_items = line.split("Starting items: ")

    return [int(item) for item in list(string_items.split(", "))]


def parse_operation(line):
    _, string_operation = line.split("Operation: new = old ")
    operation, operand = string_operation.split(" ")

    return operation, operand


def parse_test(line):
    _, divisible_by = line.split("Test: divisible by ")

    return int(divisible_by)


def parse_if_branch(line):
    _, monkey_idx = line.split(" throw to monkey ")

    return int(monkey_idx)


def get_monkey_business_level(rounds: int, is_bored_accounted=True):
    def throw_items(inspected_items):
        for (item, monkey_idx) in inspected_items:
            monkeys[monkey_idx].add_item(item)

    monkeys = parse_input_get_monkeys()
    for round in range(rounds):
        for monkey in monkeys:
            inspected_items = monkey.inspect_items(get_bored=is_bored_accounted)
            throw_items(inspected_items)

    inspection_count = sorted([monkey.total_inspected_items for monkey in monkeys])
    monkey_business = inspection_count[-1] * inspection_count[-2]

    return monkey_business


# #################################################################

print(
    f"Monkey business level after 20 rounds is {get_monkey_business_level(rounds=20)}"
)
# print(
#     f"Monkey business level after 10 000 rounds is {get_monkey_business_level(rounds=10_000, is_bored_accounted=False)}"
# )
