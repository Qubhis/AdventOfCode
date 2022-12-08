from utils import load_file

INPUT_FILE = "year_2022/inputs/day_07.txt"
COMMAND_CHAR = "$"
ROOT_DIR = "root"
SIZE = "size"


class FileSystem:
    def __init__(self):
        self.directories = {ROOT_DIR: {SIZE: 0}}
        self.current_path = [ROOT_DIR]

    def process_command(self, command):
        action, argument = command
        if action == "cd":
            self.change_directory(argument)
        elif action == "ls":
            self.process_list_output(argument)

    def change_directory(self, directory):
        if directory == "/":
            self.current_path = [ROOT_DIR]
        elif directory == "..":
            if len(self.current_path) > 1:
                self.current_path.pop()
        else:
            self.current_path.append(directory)

    def process_list_output(self, output_lines):
        for line in output_lines:
            size, name = line.split(" ")
            directory = self.get_current_directory()
            if size.isdigit():
                directory[name] = {SIZE: int(size)}
            elif size == "dir":
                directory[name] = {SIZE: 0}

    def get_current_directory(self):
        directory = self.directories
        for dir_name in self.current_path:
            directory = directory[dir_name]

        return directory

    def calculate_folder_sizes(self):
        def recursive_size_calc(directory):
            for key in directory.keys():
                if key == SIZE:
                    continue
                if is_directory(directory[key]):
                    directory[SIZE] += recursive_size_calc(directory[key])
                else:
                    directory[SIZE] += directory[key][SIZE]

            return directory[SIZE]

        recursive_size_calc(self.directories[ROOT_DIR])

    def get_root_directory(self):
        return self.directories[ROOT_DIR]

    def get_root_size(self):
        return self.directories[ROOT_DIR][SIZE]

    def get_list_of_folder_sizes(self, directory, list_of_sizes=[]):
        list_of_sizes.append(directory[SIZE])

        for key in directory.keys():
            if key != SIZE and is_directory(directory[key]):
                list_of_sizes = self.get_list_of_folder_sizes(
                    directory[key], list_of_sizes
                )

        return list_of_sizes


def transform_lines(lines):
    """returns parsed"""
    commands = []
    last_command = None
    command_buffer = []
    for line in lines:
        if line.startswith(COMMAND_CHAR):
            line_parts = line.strip().split(" ")
            if line_parts[1] == "cd":
                if last_command == "ls":
                    commands.append((last_command, tuple(command_buffer)))
                    command_buffer = []
                commands.append((line_parts[1], line_parts[2]))

            last_command = line_parts[1]
        else:
            command_buffer.append(line.strip())

    if command_buffer:
        commands.append((last_command, tuple(command_buffer)))

    return commands


def is_directory(system_entry):
    return len(system_entry.keys()) > 1


def get_sum_of_folder_with_size_at_most(max_folder_size):
    return sum([size for size in folder_sizes if size <= max_folder_size])


def get_smallest_folder_to_free_up_space_up_to(required_space):
    TOTAL_AVAILABLE_SIZE = 70_000_000
    current_unused_space = TOTAL_AVAILABLE_SIZE - file_system.get_root_size()
    space_to_free_up = required_space - current_unused_space
    smallest_dir_to_free_space = max(folder_sizes)
    for size in folder_sizes:
        if size >= space_to_free_up and size < smallest_dir_to_free_space:
            smallest_dir_to_free_space = size

    return smallest_dir_to_free_space


# ##########################################
lines = load_file(INPUT_FILE)
parsed_commands = transform_lines(lines)
file_system = FileSystem()
for command in parsed_commands:
    file_system.process_command(command)

file_system.calculate_folder_sizes()
folder_sizes = file_system.get_list_of_folder_sizes(file_system.get_root_directory())

print(
    f"Sum of all directories with total size at most 100 000: {get_sum_of_folder_with_size_at_most(100_000)}"
)
print(
    f"Size of the smallest directory to free up enough space is: {get_smallest_folder_to_free_up_space_up_to(30_000_000)}"
)
