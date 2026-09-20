from src.execution.node import Node


class MainSequence:
    def __init__(self, head: Node):
        self.ex_head = head
        self.elements_before_head = 0

    def get_current(self) -> Node:
        return self.ex_head

    def get_right(self) -> Node:
        return self.ex_head.next

    def get_left(self) -> Node:
        return self.ex_head.prev

    def jump_to(self, node: Node):
        self.ex_head = node

    def change_element_count(self, delta: int):
        self.elements_before_head += delta

    def serialize(self, aqe_file: str):
        pass

    def deserialize(self, aqe_file: str): # "re-inits" the MainSequence
        pass