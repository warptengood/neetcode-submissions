class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = [[] for _ in range(numCourses)]
        rg = [[] for _ in range(numCourses)]
        vis = [0] * numCourses
        st_points = [True] * numCourses
        for to, v in prerequisites:
            g[v].append(to)
            rg[to].append(v)
            st_points[v] = False

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

        output = []
        has_cycle = False
        for i in range(numCourses):
            if vis[i] != 0:
                continue
            if not dfs(i):
                has_cycle = True
                break
        
        if has_cycle:
            return []
        
        vis = [0] * numCourses
        
        def trav(v):
            vis[v] = 1
            for to in rg[v]:
                if vis[to] == 0:
                    trav(to)
            output.append(v)

        for i in range(numCourses):
            if st_points[i]:
                trav(i)
        return output