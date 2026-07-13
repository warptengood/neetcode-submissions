from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        col = 0
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        neighb = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not vis[i][j]:
                    q = deque()
                    q.append((i, j))
                    while len(q) > 0:
                        x, y = q.popleft()
                        vis[x][y] = True
                        for _i, _j in neighb:
                            if (
                                0 <= x + _i < n and 0 <= y + _j < m and
                                not vis[x + _i][y + _j] and grid[x + _i][y + _j] == '1'
                            ):
                                q.append((x + _i, y + _j))
                    col += 1
        return col
