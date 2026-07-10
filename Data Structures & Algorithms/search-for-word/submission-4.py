class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False] * len(row) for row in board]
        n, m = len(board), len(board[0])
        def rec(cur, x, y):
            print(cur, x, y)
            if cur == len(word):
                return True
            if x + 1 < n and board[x + 1][y] == word[cur] and not visited[x + 1][y]:
                visited[x + 1][y] = True
                res = rec(cur + 1, x + 1, y)
                if res:
                    return True
                visited[x + 1][y] = False
            if x - 1 >= 0 and board[x - 1][y] == word[cur] and not visited[x - 1][y]:
                visited[x - 1][y] = True
                res = rec(cur + 1, x - 1, y)
                if res:
                    return True
                visited[x - 1][y] = False
            if y + 1 < m and board[x][y + 1] == word[cur] and not visited[x][y + 1]:
                visited[x][y + 1] = True
                res = rec(cur + 1, x, y + 1)
                if res:
                    return True
                visited[x][y + 1] = False
            if y - 1 >= 0 and board[x][y - 1] == word[cur] and not visited[x][y - 1]:
                visited[x][y - 1] = True
                res = rec(cur + 1, x, y - 1)
                if res:
                    return True
                visited[x][y - 1] = False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    res = rec(1, i, j)
                    visited[i][j] = False
                    if res:
                        return res
        return False
