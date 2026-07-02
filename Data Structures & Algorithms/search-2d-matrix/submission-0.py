class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = []
        for m in matrix:
            a.extend(m)
        l, r = 0, len(a) - 1
        while l <= r:
            m = (l + r) // 2
            if a[m] < target:
                l = m + 1
            elif a[m] > target:
                r = m - 1
            else:
                return True
        return False