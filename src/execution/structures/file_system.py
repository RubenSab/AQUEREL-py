from pathlib import Path
import os


def validate(path:str):
    if '.' in path or '/' in path:
        raise Exception('Invalid path')


class FileSystem:
    def __init__(self, sandbox: Path):
        self.sandbox = sandbox

    def read(self, path:str) -> str:
        validate(path)
        with open(self.sandbox / Path(path)) as file:
            return file.read()

    def write(self, path:str, content:str) -> bool:
        validate(path)
        with open(self.sandbox / Path(path), "w") as file:
            return file.write(content)

    def delete(self, path:str):
        validate(path)
        os.remove(self.sandbox / Path(path))

    def exists(self, path:str) -> bool:
        validate(path)
        return os.path.exists(self.sandbox / Path(path))

