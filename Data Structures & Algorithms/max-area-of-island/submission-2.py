from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        neighb = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vis[i][j]:
                    q = deque()
                    q.append((i, j))
                    vis[i][j] = True
                    cnt = 0
                    while len(q) > 0:
                        x, y = q.popleft()
                        print(x, y)
                        cnt += 1
                        for _i, _j in neighb:
                            if (
                                0 <= x + _i < n and 0 <= y + _j < m and
                                not vis[x + _i][y + _j] and grid[x + _i][y + _j] == 1
                            ):
                                vis[x + _i][y + _j] = True
                                q.append((x + _i, y + _j))
                    # print(cnt)
                    ans = max(ans, cnt)
        # for v in vis:
        #     print(v)
        return ans
