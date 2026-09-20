import re

class Parser:
    def __init__(self, source_code: list[str]):
        self.main_seq = []
        self.source_code = source_code
        self.brackets_stack = []

    def parse(self):
        # TODO: escapes
        for i, line in enumerate(self.source_code):
            self.main_seq.extend([
                self.make_node(token, i) for token
                in re.findall(r"'[^']*'|[^\s()]+|[()]", line)
            ])

    def make_node(self, token: str, line_index: int):
        return token


p = Parser(["'a h hgj' d()('c q' 'a' d)'c q'"])
p.parse()
print(p.main_seq)