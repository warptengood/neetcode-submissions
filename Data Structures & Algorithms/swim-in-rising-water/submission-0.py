class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        INF = int(2e9)
        n, m = len(grid), len(grid[0])
        dist = [[INF] * m for _ in range(n)]
        dist[n - 1][m - 1] = grid[n - 1][m - 1]
        heap = []
        heap.append((dist[n - 1][m - 1], n - 1, m - 1))
        side = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while len(heap) > 0:
            d, x, y = heapq.heappop(heap)
            for i, j in side:
                if (
                    0 <= x + i < n and 0 <= y + j < m and
                    dist[x + i][y + j] > max(grid[x + i][y + j], dist[x][y])
                ):
                    dist[x + i][y + j] = max(grid[x + i][y + j], d)
                    heapq.heappush(heap, (dist[x + i][y + j], x + i, y + j))
        
        return dist[0][0]