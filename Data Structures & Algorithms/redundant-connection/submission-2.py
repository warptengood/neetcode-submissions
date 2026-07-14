class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = -1
        g = [[] for _ in range(1000)]
        par = [-1] * 1000
        map = {}
        for i, e in enumerate(edges):
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
            a, b = e
            if a > b:
                a, b = b, a
            map[(a, b)] = i
            root = max(root, e[0], e[1])
        n = (root + 1)
        vis = [0] * n

        cycle_range = []
        def dfs(v, p=-1):
            vis[v] = 1
            par[v] = p
            for to in g[v]:
                if to != p:
                    if vis[to] == 0:
                        dfs(to, v)
                    elif vis[to] == 1:
                        cycle_range.append([v, to])
            vis[v] = 2
        
        dfs(root)
        st, nd = cycle_range[-1]
        cycle = []
        cur = st
        while cur != nd:
            cycle.append(cur)
            cur = par[cur]

        cycle.append(nd)
        cycle.append(st)

        max_ans = -1
        for i in range(len(cycle) - 1):
            a, b = cycle[i], cycle[i + 1]
            if a > b:
                a, b = b, a
            max_ans = max(max_ans, map[(a, b)])
        
        return edges[max_ans]