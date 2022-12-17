from dataclasses import dataclass, field

from utils import load_file


INPUT_FILE = "year_2022/inputs/day_10.txt"
NOOP = "noop"
ADDX = "addx"


@dataclass
class CPU:
    register: int = 1
    cycle: int = 0
    reporting_cycles: list[int] = field(
        default_factory=lambda: [20, 60, 100, 140, 180, 220]
    )
    reported_signals: list[int] = field(default_factory=list)

    def process_instruction(self, instruction, register):
        INSTRUCTION_TIME = {NOOP: 1, ADDX: 2}
        cycles_time = INSTRUCTION_TIME[instruction]
        for _ in range(cycles_time):
            self.cycle += 1
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


def get_signal_strength_part_1():
    cpu = CPU()
    for line in lines:
        line_parts = line.split(" ")
        instruction = line_parts[0]
        register = int(line_parts[1]) if len(line_parts) > 1 else 0

        cpu.process_instruction(instruction=instruction, register=register)

    return sum(cpu.get_reported_signals())


# #################################################################3
lines = [line.strip() for line in load_file(INPUT_FILE)]
print(f"Sum of the six signal strengths is {get_signal_strength_part_1()}.")
