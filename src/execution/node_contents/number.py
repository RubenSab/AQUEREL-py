from src.execution.node_contents.node_content import NodeContent


class Number(NodeContent):
    def __init__(self, value: float):
        super().__init__()
        self.value = value