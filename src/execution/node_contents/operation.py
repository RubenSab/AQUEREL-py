from src.execution.node_contents.node_content import NodeContent

OPERATIONS = {}

class Operation(NodeContent):
    def __init__(self, token: str):
        super().__init__(token)
        self.operation = OPERATIONS[token]