from src.execution.node_contents.node_content import NodeContent


class QuotedString(NodeContent):
    def __init__(self, value: str):
        super().__init__()
        self.value = value