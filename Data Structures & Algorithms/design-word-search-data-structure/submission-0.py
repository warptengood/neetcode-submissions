class Node:
    def __init__(self):
        self.ex = False
        self.nodes = [None] * 26

    def __getitem__(self, index):
        return self.nodes[index]

    def __iter__(self):
        return iter(self.nodes)
    
    def __setitem__(self, index, value):
        self.nodes[index] = value

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for w in word:
            id = ord(w) - 97
            if cur_node[id] is None:
                cur_node[id] = Node()
            cur_node = cur_node[id]
        cur_node.ex = True

    def find(self, node, id, word):
        if id == len(word):
            return node.ex
        letter_id = ord(word[id]) - 97
        if word[id] != '.':
            if node[letter_id] is None:
                return False
            else:
                return self.find(node[letter_id], id + 1, word)
        else:
            for i in range(26):
                if node[i] is not None:
                    res = self.find(node[i], id + 1, word)
                    if res:
                        return True
            return False

    def search(self, word: str) -> bool:
        return self.find(self.root, 0, word)
