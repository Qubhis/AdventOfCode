from utils import load_file


INPUT_FILE = "year_2022/day_01_input.txt"

lines = load_file(INPUT_FILE)
calories = [line.replace("\n", "") for line in lines]

elf_calories_count = []
current_elf_calories = 0
for calorie_value in calories:
    if calorie_value == "":
        elf_calories_count.append(current_elf_calories)
        current_elf_calories = 0
        continue
    current_elf_calories += int(calorie_value)
else:
    elf_calories_count.append(current_elf_calories)

elf_calories_count.sort(reverse=True)

print(f"Top calorie count for single elf: {elf_calories_count[0]}")
print(f"Top three calories counts: {sum(elf_calories_count[0:3])}")
