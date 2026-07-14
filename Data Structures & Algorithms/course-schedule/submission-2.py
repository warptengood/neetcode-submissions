class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        vis = [0] * numCourses
        for to, v in prerequisites:
            g[v].append(to)

        def dfs(v):
            vis[v] = 1
            res = True
            for to in g[v]:
                if vis[to] == 1:
                    return False
                if vis[to] == 0:
                    res &= dfs(to)
            vis[v] = 2
            return res

        for i in range(numCourses):
            if vis[i] != 0:
                continue
            if not dfs(i):
                return False
        
        return True