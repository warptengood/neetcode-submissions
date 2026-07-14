class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        vis = [False] * n

        def dfs(v):
            vis[v] = True
            for to in g[v]:
                if not vis[to]:
                    dfs(to)

        ans = 0

        for i in range(n):
            if not vis[i]:
                ans += 1
                dfs(i)
        
        return ans