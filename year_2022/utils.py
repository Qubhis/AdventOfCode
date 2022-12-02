def load_file(filepath):
    """reads file and returns array of lines"""
    with open(filepath, "r") as file:

        return file.readlines()
