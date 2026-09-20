from pathlib import Path
import re

from src.execution.node import Node
from src.execution.node_contents.node_content import NodeContent
from src.execution.node_contents.quoted_string import QuotedString


def make_node(token: str, line_index: int) -> Node:
    node = None
    if type(token)==str:
        node = Node(QuotedString(token))
        node.content.line_index = line_index
    return node


class Interpreter:
    def __init__(self):
        self.first_node = None

    def parse(self, source_path: Path):
        with open(source_path, "r") as f:
            lines = f.readlines()
        # TODO: escapes
        prev_node = None
        for i, line in enumerate(lines):
            tokens = re.findall(r"'[^']*'|[^\s()]+|[()]", line) # still doesn't support multi line strings
            for t in tokens:
                if self.first_node is None:
                    self.first_node = make_node(t, i)
                    prev_node = self.first_node
                else:
                    next_node = make_node(t, i)
                    prev_node.append(next_node)
                    prev_node = next_node


i = Interpreter()
i.parse(Path('/home/ruben/AQUEREL/src/testing/test.aqs'))
print(i.first_node.str_chain())