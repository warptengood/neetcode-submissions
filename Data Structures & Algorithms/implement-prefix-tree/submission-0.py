class Node:
    def __init__(self):
        self.ex = 0
        self.nodes = [None] * 26


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur_node = self.root
        for w in word:
            id = ord(w) - 97
            if cur_node.nodes[id] is None:
                cur_node.nodes[id] = Node()
            cur_node = cur_node.nodes[id]
        cur_node.ex = 1

    def search(self, word: str) -> bool:
        cur_node = self.root
        for w in word:
            id = ord(w) - 97
            if not cur_node.nodes[id]:
                return False
            cur_node = cur_node.nodes[id]
        return cur_node.ex == 1

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for w in prefix:
            id = ord(w) - 97
            if not cur_node.nodes[id]:
                return False
            cur_node = cur_node.nodes[id]
        return True
        