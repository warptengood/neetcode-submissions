from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        INF = int(1e9)

        side = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        q = deque()
        vis  = [[False] * m for _ in range(n)]

        for i in range(n):
            if board[i][0] == 'O':
                q.append((i, 0))
                vis[i][0] = True
            if board[i][m - 1] == 'O':
                q.append((i, m - 1))
                vis[i][m - 1] = True

        for j in range(m):
            if board[0][j] == 'O':
                q.append((0, j))
                vis[0][j] = True
            if board[n - 1][j] == 'O':
                q.append((n - 1, j))
                vis[n - 1][j] = True
            
        while len(q) > 0:
            x, y = q.popleft()
            for a, b in side:
                if (
                    0 <= x + a < n and 0 <= y + b < m and
                    not vis[x + a][y + b] and board[x + a][y + b] == 'O'
                ):
                    vis[x + a][y + b] = True
                    q.append((x + a, y + b))
        
        for i in range(n):
            for j in range(m):
                board[i][j] = 'O' if vis[i][j] else 'X'