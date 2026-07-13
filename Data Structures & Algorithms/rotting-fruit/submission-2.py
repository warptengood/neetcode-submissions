class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        sides = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])
        INF = int(1e9)
        dist = [[0 if grid[i][j] == 2 else INF for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q = deque() 
                    q.append((i, j))
                    while len(q) > 0:
                        x, y = q.popleft()
                        for _i, _j in sides:
                            if 0 <= x + _i < n and 0 <= y + _j < m and grid[x + _i][y + _j] > 0 and dist[x + _i][y + _j] > 1 + dist[x][y]:
                                dist[x + _i][y + _j] = 1 + dist[x][y]
                                q.append((x + _i, y + _j))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans = max(ans, dist[i][j])
        for d in dist:
            print(d)
        return -1 if ans == INF else ans