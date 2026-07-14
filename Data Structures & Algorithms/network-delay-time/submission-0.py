class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        dist = [INF] * n
        g = [[] for _ in range(n)]
        for u, v, t in times:
            g[u-1].append((v-1, t))
        dist[k - 1] = 0

        vis = [(dist[k - 1], k - 1)]
        while len(vis) > 0:
            d, v = heapq.heappop(vis)
            for to, w in g[v]:
                if dist[to] > d + w:
                    dist[to] = d + w
                    heapq.heappush(vis, (dist[to], to))
        res = sorted(dist)[-1]
        return res if res != INF else -1