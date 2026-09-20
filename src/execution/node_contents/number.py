from src.execution.node_contents.node_content import NodeContent


class Number(NodeContent):
    def __init__(self, token: str):
        super().__init__(token)
        self.value = float(token)