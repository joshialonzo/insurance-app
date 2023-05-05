from pathlib import Path


class Storage:
    def __init__(self, file):
        self.file = file

    @property
    def file_path(self):
        home = Path.home()
        folder = home / "data" / "insurance"
        return folder / self.file

    def file_path_exists(self):
        return self.file_path.exists()
