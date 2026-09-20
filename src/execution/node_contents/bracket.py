from src.execution.node_contents.node_content import NodeContent


class Bracket(NodeContent):
    def __init__(self, is_open = True):
        super().__init__()
        self.is_open = is_open
        if not is_open:
            self.elements_inside = 0
        self.corresponding = None # bracket