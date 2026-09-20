from src.execution.node_contents.node_content import NodeContent


class Operation(NodeContent):
    def __init__(self, operation: str):
        super().__init__()
        self.operation = operation # should have been done with an enum