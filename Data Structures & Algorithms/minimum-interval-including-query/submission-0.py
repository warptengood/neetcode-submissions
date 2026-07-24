class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(query, i) for i, query in enumerate(queries)]
        queries.sort()
        Nq = len(queries)
        intervals.sort(key=lambda i: i[1] - i[0] + 1)
        INF = int(1e9)
        tree = [INF] * (Nq * 4)
        treeMin = [-1] * (Nq * 4)

        def push(v, vl, vr):
            if treeMin[v] != -1:
                if tree[v] > treeMin[v]:
                    tree[v] = treeMin[v]
                    if vl != vr:
                        treeMin[v * 2 + 1] = treeMin[v]
                        treeMin[v * 2 + 2] = treeMin[v]
                    treeMin[v] = -1

        def modify(v, vl, vr, l, r, val):
            push(v, vl, vr)
            if r < vl or vr < l:
                return
            if l <= vl and vr <= r:
                treeMin[v] = val
                push(v, vl, vr)
                return
            vm = (vl + vr) >> 1
            modify(v * 2 + 1, vl, vm, l, r, val)
            modify(v * 2 + 2, vm + 1, vr, l, r, val)
            tree[v] = max(tree[v * 2 + 1], tree[v * 2 + 2])

        def get(v, vl, vr, index):
            push(v, vl, vr)
            if vl == vr:
                return tree[v]
            vm = (vl + vr) >> 1
            if index <= vm:
                return get(v * 2 + 1, vl, vm, index)
            else:
                return get(v * 2 + 2, vm + 1, vr, index)

        def out(v, vl, vr):
            push(v, vl, vr)
            if vl == vr:
                print(tree[v], end = ' ')
                return
            vm = (vl + vr) >> 1
            out(v * 2 + 1, vl, vm)
            out(v * 2 + 2, vm + 1, vr)

        def binl(target):
            l, r = 0, Nq - 1
            ans = -1
            while l <= r:
                m = (l + r) >> 1
                if queries[m][0] < target:
                    l = m + 1
                else:
                    ans = m
                    r = m - 1
            return ans

        def binr(target):
            l, r = 0, Nq - 1
            ans = -1
            while l <= r:
                m = (l + r) >> 1
                if queries[m][0] <= target:
                    ans = m
                    l = m + 1
                else:
                    r = m - 1
            return ans

        for i in intervals:
            left = binl(i[0])
            right = binr(i[1])
            if left == -1 or right == -1:
                continue
            modify(0, 0, Nq - 1, left, right, i[1] - i[0] + 1)

        result = [-1] * Nq

        for i in range(Nq):
            val = get(0, 0, Nq - 1, i)
            if val != INF:
                result[queries[i][1]] = val

        return result