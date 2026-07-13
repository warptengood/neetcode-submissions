from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pac_st_pos, atl_st_pos = [], []
        pac, atl = [], []
        INF = int(1e9)

        for i in range(n):
            temp_pac = []
            temp_atl = []
            for j in range(m):
                temp_atl.append(0 if j == m - 1 or i == n - 1 else INF)
                temp_pac.append(0 if j == 0 or i == 0 else INF)
                if i == 0 or j == 0:
                    pac_st_pos.append((i, j))
                if i == n - 1 or j == m - 1:
                    atl_st_pos.append((i, j))
            pac.append(temp_pac)
            atl.append(temp_atl)

        side = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(grid, st_pos):
            q = deque()
            q.extend(st_pos)
            while len(q) > 0:
                x, y = q.popleft()
                for i, j in side:
                    if not (0 <= x + i < n and 0 <= y + j < m):
                        continue
                    if heights[x + i][y + j] >= heights[x][y] and grid[x + i][y + j] > heights[x][y] + 1:
                        grid[x + i][y + j] = heights[x][y] + 1
                        q.append((x + i, y + j))
        
        bfs(pac, pac_st_pos)
        bfs(atl, atl_st_pos)

        output = []
        
        for i in range(n):
            for j in range(m):
                if pac[i][j] != INF and atl[i][j] != INF:
                    output.append([i, j])
        return output