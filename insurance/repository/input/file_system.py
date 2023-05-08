import csv
from pathlib import Path


class FileSystem:
    def __init__(self, file):
        self.file = file

    @property
    def file_path(self):
        home = Path.home()
        folder = home / "data" / "insurance"
        return folder / self.file

    def file_path_exists(self):
        return self.file_path.exists()

    def file_path_content(self):
        """
        Read the content of the CSV file.
        """
        with open(self.file_path, newline="", encoding="latin-1") as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)

    def file_path_lines(self):
        """
        Read the content of the CSV file.
        """
        if not self.file_path_exists():
            return []

        lines = self.file_path_content()
        return lines[2:]
