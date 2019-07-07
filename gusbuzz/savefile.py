from pathlib import Path

from gusbuzz.assets.settings import SAVE_LOCATION


class Savefile:

    def __init__(self):
        self.file_path = Path('.') / SAVE_LOCATION
        if self.file_path.exists():
            try:
                self.high_score = int(self.file_path.read_text())
            except ValueError:
                # File does not contain a number
                self.high_score = 0
        else:
            self.file_path.touch()
            self.high_score = 0

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.file_path.resolve()}'

    def save_file(self):
        self.file_path.write_text(str(self.high_score))

    def delete_file(self):
        self.file_path.unlink()
