import csv
from pathlib import Path


class FileSystem:
    def __init__(
        self,
        file: str,
        folder: str = "data/insurance",
        first_row: int = 2,
    ):
        self.file = file
        self.folder = folder
        self.first_row = first_row

    @property
    def file_path(self):
        home = Path.home()
        folder = home / self.folder
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
        return lines[self.first_row:]
