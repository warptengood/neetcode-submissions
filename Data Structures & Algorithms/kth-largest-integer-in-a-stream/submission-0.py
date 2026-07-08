class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.sz = 2001
        self.mod = 1000
        self.k = k
        self.tree = [0] * (self.sz * 4)
        for n in nums:
            self._add(0, 0, self.sz - 1, n + self.mod)

    def add(self, val: int) -> int:
        self._add(0, 0, self.sz - 1, val + self.mod)
        return self.get(0, 0, self.sz - 1, self.k) - self.mod

    def get(self, v, vl, vr, k):
        if vl == vr:
            return vl
        vm = (vl + vr) >> 1
        if k <= self.tree[v * 2 + 2]:
            return self.get(v * 2 + 2, vm + 1, vr, k)
        else:
            return self.get(v * 2 + 1, vl, vm, k - self.tree[v * 2 + 2])
         

    def _add(self, v, vl, vr, val):
        if vl == vr:
            self.tree[v] += 1
            return
        vm = (vl + vr) >> 1
        if val <= vm:
            self._add(v * 2 + 1, vl, vm, val)
        else:
            self._add(v * 2 + 2, vm + 1, vr, val)
        
        self.tree[v] = self.tree[v * 2 + 1] + self.tree[v * 2 + 2]