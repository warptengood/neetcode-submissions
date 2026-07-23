class Solution:

    def modify(self, v, vl, vr, pos, val, tree):
        if vl == vr:
            tree[v] = val
            return
        vm = (vl + vr) >> 1
        if pos <= vm:
            self.modify(v * 2 + 1, vl, vm, pos, val, tree)
        else:
            self.modify(v * 2 + 2, vm + 1, vr, pos, val, tree)
        tree[v] = min(tree[v * 2 + 1], tree[v * 2 + 2])

    def get(self, v, vl, vr, l, r, tree):
        if l <= vl and vr <= r:
            return tree[v]
        if r < vl or vr < l:
            return int(1e9)
        
        vm = (vl + vr) >> 1
        q1 = self.get(v * 2 + 1, vl, vm, l, r, tree)
        q2 = self.get(v * 2 + 2, vm + 1, vr, l, r, tree)
        return min(q1, q2)

    def out(self, v, vl, vr, tree):
        if vl == vr:
            print(tree[v], end=', ')
        else:
            vm = (vl + vr) >> 1
            self.out(v * 2 + 1, vl, vm, tree)
            self.out(v * 2 + 2, vm + 1, vr, tree)

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        INF = int(1e9)
        tree = [INF] * (4 * n)
        dp = [INF] * n
        dp[n - 1] = 0
        self.modify(0, 0, n - 1, n - 1, 0, tree)
        for i in range(n - 2, -1, -1):
            r = min(i + nums[i], n - 1)
            dp[i] = min(dp[i], self.get(0, 0, n - 1, i + 1, r, tree) + 1)
            self.modify(0, 0, n - 1, i, dp[i], tree)
        return dp[0]