class SegTree:
    def __init__(self, n: int) -> None:
        self._tree_size = n
        self._tree = [0] * (1 << (n.bit_length() + 1))

    def get(self) -> int:
        return self._get(0, 0, self._tree_size - 1)

    def _get(self, v: int, vl: int, vr: int) -> int:
        if vl == vr:
            return vl
        vm = (vr + vl) >> 1
        if self._tree[v * 2 + 2] > 0:
            return self._get(v * 2 + 2, vm + 1, vr)
        else:
            return self._get(v * 2 + 1, vl, vm)
    
    def update(self, pos: int, val: int) -> int:
        self._update(0, 0, self._tree_size - 1, pos, val)
    
    def _update(self, v: int, vl: int, vr: int, pos: int, val: int) -> None:
        if vl == vr:
            self._tree[v] += val
            return
        vm = (vr + vl) >> 1
        if vl <= pos <= vm:
            self._update(v * 2 + 1, vl, vm, pos, val)
        else:
            self._update(v * 2 + 2, vm + 1, vr, pos, val)
        self._tree[v] = self._tree[v * 2 + 1] + self._tree[v * 2 + 2]
    


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        modifier = 10000
        tree = SegTree(modifier * 2 + 1)
        nums = [n + modifier for n in nums]
        for i in range(k):
            tree.update(nums[i], 1)

        res = []
        l, r = 0, k - 1
        while r < len(nums):
            res.append(tree.get() - modifier)
            if r == len(nums) - 1:
                break
            tree.update(nums[l], -1)
            l += 1
            r += 1
            tree.update(nums[r], 1)
        return res