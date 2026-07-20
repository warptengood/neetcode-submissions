from bisect import bisect_left, bisect_right
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        negs = []
        segs = []
        INF = -int(2e9)
        ans = INF
        for i in range(n):
            ans = max(ans, nums[i])
            if nums[i] < 0:
                negs.append(i)
                r += 1
            elif nums[i] == 0:
                segs.append((l, r))
                l, r = i + 1, i + 1
            else:
                r += 1
            if nums[i] != 0 and i == n - 1:
                segs.append((l, r))

        for l, r in segs:
            if l >= r:
                continue
            nl = bisect_left(negs, l)
            nr = bisect_right(negs, r)
            p = []
            for i in range(l, r):
                p.append(nums[i] * (1 if len(p) == 0 else p[-1]))
            if (nr - nl) % 2 == 0:
                ans = max(ans, p[-1])
                continue

            for i in range(nl, nr):
                pivot = negs[i]
                if pivot + 1 <= r - 1 and 0 <= pivot < n and 0 <= r - 1 < n:
                    ans = max(ans, p[r-1-l] // p[pivot-l])
                if l <= pivot - 1 and 0 <= pivot-1 < n and 0 <= l < n:
                    ans = max(ans, p[pivot-1-l])
        
        return ans