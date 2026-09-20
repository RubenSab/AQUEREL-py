from src.execution.node_contents.node_content import NodeContent


class Name(NodeContent):
    def __init__(self, string: str):
        super().__init__()
        self.string = string