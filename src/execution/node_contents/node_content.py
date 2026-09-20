class NodeContent:
    def __init__(self, token: str):
        self.line_index = None
        self.token = token

    def __str__(self):
        return self.token

    def debug_str(self):
        return self.token + f', line {self.line_index}' if self.line_index is not None else ''