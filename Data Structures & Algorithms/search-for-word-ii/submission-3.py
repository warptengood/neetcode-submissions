from  typing import List

class Node:
    def __init__(self):
        self.st = None
        self.nodes = [None] * 26

    def __iter__(self):
        return iter(self.nodes)

    def __getitem__(self, key):
        return self.nodes[ord(key) -  97]

    def __setitem__(self, key, value):
        self.nodes[ord(key) -  97] = value

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        
        root = Node()
        for word in words:
            cur_node = root
            for w in word:
                if cur_node[w] is None:
                    cur_node[w] = Node()
                cur_node = cur_node[w]
            cur_node.st = word
        
        output = set()
        vis = [[False] * m for _ in range(n)]

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def rec(x, y, node):
            vis[x][y] = True
            if node.st is not None:
                output.add(node.st)
            for i, j in neighbors:
                if (
                    0 <= x + i < n and 0 <= y + j < m and
                    node[board[x + i][y + j]] is not None and 
                    not vis[x + i][y + j]
                ):
                    rec(x + i, y + j, node[board[x + i][y + j]])
            vis[x][y] = False

        for i in range(n):
            for j in range(m):
                if root[board[i][j]] is not None:
                    rec(i, j, root[board[i][j]])
        
        return list(output)
