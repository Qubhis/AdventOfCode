from utils import load_file

INPUT_FILE = "year_2022/inputs/day_07.txt"
JSON_FILE = "year_2022/output/day_07.json"
COMMAND_CHAR = "$"
ROOT_DIR = "root"


class FileSystem:
    def __init__(self):
        self.directories = {ROOT_DIR: {"size": 0}}
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
            if line[0].isdigit():
                directory[name] = {"size": int(size)}
            elif line[:3] == "dir":
                directory[name] = {"size": 0}

    def get_current_directory(self):
        directory = self.directories
        for dir_name in self.current_path:
            directory = directory[dir_name]
        else:
            return directory

    def calculate_folder_sizes(self):
        def recursive_size_calc(directory):
            for key in directory.keys():
                if key == "size":
                    continue
                if len(directory.get(key, {"size": 0}).keys()) > 1:
                    directory["size"] += recursive_size_calc(directory[key])
                else:
                    directory["size"] += directory[key]["size"]
            else:
                return directory["size"]

        directory = self.directories[ROOT_DIR]
        recursive_size_calc(directory)

    def getJSON(self):
        import json

        with open(JSON_FILE, "w+") as file:
            json.dump(self.directories, file, indent=2)


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

    return commands


def get_sum_of_folder_with_size_at_most_100_000():
    parsed_commands = transform_lines(lines)
    file_system = FileSystem()
    for command in parsed_commands:
        file_system.process_command(command)

    file_system.calculate_folder_sizes()
    file_system.getJSON()


# ##########################################
lines = load_file(INPUT_FILE)
print(
    f"Sum of all directories with total size at most 100 000: {get_sum_of_folder_with_size_at_most_100_000()}"
)
