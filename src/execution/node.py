from src.execution.node_contents.node_content import NodeContent


def extract(start: Node, end: Node) -> Node:
    if start.prev:
        start.prev.next = end.next
    if end.next:
        end.next.prev = start.prev
    start.prev = None
    end.next = None
    return start


def replace(to_replace: Node, start: Node, end: Node):
    if to_replace.prev:
        to_replace.prev.next = start
        start.prev = to_replace.prev
    if to_replace.next:
        to_replace.next.prev = end
        end.next = to_replace.next
    to_replace.prev = None
    to_replace.next = None


def splice_after(location: Node, start: Node, end: Node):
    end.next = location.next
    location.next = start
    location.next.prev = end
    start.prev = location


class Node:
    def __init__(self, content: NodeContent, prev: Node):
        self.content = content
        self.prev = prev
        self.next = None

    def append(self, next_node: Node):
        self.next = next_node

    def __str__(self):
        return str(self.content)

    def str_chain(self):
        node = self
        strings = []
        while node:
            strings.append(str(node))
            node = node.next
        return " ".join(strings)