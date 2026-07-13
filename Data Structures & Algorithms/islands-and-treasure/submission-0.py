from  typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        sides = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q = deque()
                    q.append((i, j))
                    while len(q) > 0:
                        x, y = q.popleft()
                        for _i, _j in sides:
                            if 0 <= x + _i < n and 0 <= y + _j < m and grid[x + _i][y + _j] > 1 + grid[x][y]:
                                grid[x + _i][y + _j] = 1 + grid[x][y]
                                q.append((x + _i, y + _j))