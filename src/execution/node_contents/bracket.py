from src.execution.node_contents.node_content import NodeContent


class Bracket(NodeContent):
    def __init__(self, token: str):
        super().__init__(token)
        self.value = token
        if self.value == ')':
            self.elements_inside = 0
        self.corresponding = None # opposite bracket