from src.execution.node import Node


class Namespace:
    def __init__(self):
        self.space = dict()

    def map(self, name:str, start:Node):
        self.space[name] = start

    def unmap(self, name:str):
        self.space.pop(name)

    def check(self, name:str) -> bool:
        return name in self.space

    def get(self, name:str) -> Node:
        return self.space[name]