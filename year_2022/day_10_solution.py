from dataclasses import dataclass, field

from utils import load_file


INPUT_FILE = "year_2022/inputs/day_10.txt"
NOOP = "noop"
ADDX = "addx"


@dataclass
class CRTScreen:
    height: int = 6
    width: int = 40
    pixel_rows: list[list[str]] = field(default_factory=list, init=False)

    def __post_init__(self):
        self.pixel_rows = [["."] * self.width for row in range(self.height)]

    def print_screen(self):
        screen_output = ""
        for row in self.pixel_rows:
            screen_output += "".join(row) + "\n"

        print(screen_output)

    def lit_pixel(self, row, col):
        self.pixel_rows[row][col] = "#"


@dataclass
class CPU:
    register: int = 1
    cycle: int = 0
    reporting_cycles: list[int] = field(
        default_factory=lambda: [20, 60, 100, 140, 180, 220]
    )
    reported_signals: list[int] = field(default_factory=list)
    screen: CRTScreen = field(init=False)

    def __post_init__(self):
        self.screen = CRTScreen()

    def process_instruction(self, instruction, register):
        INSTRUCTION_TIME = {NOOP: 1, ADDX: 2}
        cycles_time = INSTRUCTION_TIME[instruction]
        for _ in range(cycles_time):
            self.cycle += 1
            self.draw_pixel()
            if self.is_reporting_cycle():
                self.collect_signal_strength()

        if instruction == ADDX:
            self.register += register

    def is_reporting_cycle(self):
        return self.cycle in self.reporting_cycles

    def collect_signal_strength(self):
        signal_strength = self.cycle * self.register
        self.reported_signals.append(signal_strength)

    def get_reported_signals(self):
        return self.reported_signals

    def show_screen(self):
        self.screen.print_screen()

    def draw_pixel(self):
        row = int((self.cycle) / self.screen.width)
        column = self.cycle % self.screen.width - 1
        if column in self.get_sprite_position():
            self.screen.lit_pixel(row=row, col=column)

    def get_sprite_position(self):
        return (self.register - 1, self.register, self.register + 1)


# #################################################################3
lines = [line.strip() for line in load_file(INPUT_FILE)]
cpu = CPU()
for line in lines:
    line_parts = line.split(" ")
    instruction = line_parts[0]
    register = int(line_parts[1]) if len(line_parts) > 1 else 0

    cpu.process_instruction(instruction=instruction, register=register)

print(f"Sum of the six signal strengths is {sum(cpu.get_reported_signals())}.\n")
cpu.show_screen()
