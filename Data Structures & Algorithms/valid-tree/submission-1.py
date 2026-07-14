class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = [[] for _ in range(n)]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        
        vis = [False] * n

        def dfs(v, p=-1):
            vis[v] = True
            res = True
            for to in g[v]:
                if to != p:
                    if vis[to] == True:
                        return False
                    res &= dfs(to, v)
            return res

        ans = dfs(0)

        for v in vis:
            if not v:
                return False

        return ans 