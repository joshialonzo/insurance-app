from insurance.repository.input.file_system import FileSystem


def get_first_line():
    """Retrieve first line from file"""
    file = "payments.csv"
    file_system = FileSystem(file=file)
    lines = file_system.file_path_lines()
    first_line = lines[0]
    return first_line
