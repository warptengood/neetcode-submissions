class Node:
    def __init__(self, key=0):
        self._key = key 
        self._str = False
        self._nodes = [None] * 26
    
    def out(self, depth):
        print(f"[{self._key}]:")
        for i in range(26):
            if self._nodes[i] is not None:
                print(f"{'     ' * depth}|-{chr(i + 97)}-> ", end='')
                self._nodes[i].out(depth + 1)

class Solution:

    cnt = 0

    def add(self, root, word):
        cur = root
        for w in word:
            id = ord(w) - 97
            if cur._nodes[id] is None:
                cur._nodes[id] = Node(self.cnt)
                self.cnt += 1
            cur = cur._nodes[id]
        cur._str = True

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Node(self.cnt)
        self.cnt += 1
        for word in wordDict:
            self.add(root, word)

        # root.out(0)
        dp = [[-1] * self.cnt for _ in range(len(s))]

        def rec(cur_i, node):
            # print("Current char:", "EOS" if cur_i == len(s) else s[cur_i], "Node key:", node._key)
            if cur_i == len(s):
                return node._str
            
            if dp[cur_i][node._key] != -1:
                return dp[cur_i][node._key]

            if node._nodes[ord(s[cur_i]) - 97] is None:
                return False

            dp[cur_i][node._key] = False
            if node._nodes[ord(s[cur_i]) - 97]._str:
                dp[cur_i][node._key] = rec(cur_i + 1, root)

            dp[cur_i][node._key] |= rec(cur_i + 1, node._nodes[ord(s[cur_i]) - 97])

            return dp[cur_i][node._key]

        return rec(0, root)