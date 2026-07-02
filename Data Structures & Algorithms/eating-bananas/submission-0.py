class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 1000000000
        ans = r

        def check(k):
            hr = 0
            for p in piles:
                hr += (p // k) + (p % k != 0)
            return hr <= h

        while l <= r:
            m = (l + r) // 2
            if check(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans