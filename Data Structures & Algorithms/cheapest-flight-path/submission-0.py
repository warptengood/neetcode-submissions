class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for i, j, c in flights:
            g[j].append((i, c))
        
        INF = int(2e9)
        dist = [(INF, INF) for _ in range(n)]
        q = []
        dist[dst] = (0, 0)
        q.append((dist[dst], dst))
        while len(q) > 0:
            d, v = heapq.heappop(q)
            distance, steps = d
            for to, c in g[v]:
                if dist[to][0] > distance + c and steps + 1 <= k + 1:
                    dist[to] = (distance + c, steps + 1)
                    heapq.heappush(q, (dist[to], to))
        if dist[src][0] == INF:
            return -1
        return dist[src][0]