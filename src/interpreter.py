from pathlib import Path
import re

from src.execution.node import Node
from src.execution.node_contents.bracket import Bracket
from src.execution.node_contents.name import Name
from src.execution.node_contents.number import Number
from src.execution.node_contents.operation import Operation, OPERATIONS
from src.execution.node_contents.quoted_string import QuotedString


def make_node(token: str, line_index: int) -> Node:
    node_content = None
    if token == '(' or token == ')':
        node_content = Bracket(token)
    elif token.replace('.','',1).replace('-', '1').isdigit():
        node_content = Number(token)
    elif token.startswith("'") and token.endswith("'"):
        node_content = QuotedString(token)
    elif token in OPERATIONS:
        node_content = Operation(token)
    else:
        node_content = Name(token)
    node_content.line_index = line_index + 1
    return Node(node_content)



class Interpreter:
    def __init__(self):
        self.head = None


    def parse(self, source_path: Path):
        with open(source_path, "r") as f:
            lines = f.readlines()
        if not lines:
            return
        bracket_stack = []
        prev_node = None
        for i, line in enumerate(lines):
            tokens = re.findall(r"'[^']*'|[^\s()]+|[()]", line) # still doesn't support escapes multi line strings
            for t in tokens:
                current = make_node(t, i)
                if isinstance(current.content, Bracket):
                    bracket = current.content
                    if bracket.value == ')' and bracket_stack and bracket_stack[-1].value == '(':
                        corresponding = bracket_stack.pop()
                        bracket.corresponding = corresponding
                        corresponding.corresponding = bracket
                    else:
                        bracket_stack.append(bracket)
                if self.head is None:
                    self.head = current
                else:
                    prev_node.append(current)
                prev_node = current


    def interpret(self):
        if self.head is None:
            return True
        while self.head is not None:
            try:
                self.head = self.head.execute()
            # possible side effects:
            #   calls self.head.jump_to(...)
            #   manipulates the man sequence
            #   updates counts of elements before head
            #   manipulates the namespace
            #   interacts with the I/O
            #   interacts with the RNG
            #   queries the clock
            except Exception as e:
                print(f'Error during execution of {self.head.content.debug_str()}: {e}')
                return False
        return True


i = Interpreter()
i.parse(Path('/home/ruben/AQUEREL/src/testing/test.aqs'))
i.interpret()