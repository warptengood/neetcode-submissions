class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        N = n * m
        in_degree = [0] * N
        side = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        g = [[] for _ in range(m * n)]
        for i in range(n):
            for j in range(m):
                for x, y in side:
                    if 0 <= i + x < n and 0 <= j + y < m:
                        if matrix[i][j] < matrix[i + x][j + y]:
                            u, v = i * m + j, (i + x) * m + (j + y)
                            g[u].append(v)
                            in_degree[v] += 1

        q = deque()
        INF = -int(1e9)
        dist = [INF] * N
        for i in range(N):
            if in_degree[i] == 0:
                q.append(i)
                dist[i] = 0

        topsort = []
                
        while (len(q) > 0):
            v = q.popleft()
            topsort.append(v)
            for to in g[v]:
                in_degree[to] -= 1
                if in_degree[to] == 0:
                    q.append(to)

        for v in topsort:
            if dist[v] == INF:
                continue
            for to in g[v]:
                dist[to] = max(dist[to], dist[v] + 1)

        ans = max(dist) if len(dist) else 0
        return ans + 1