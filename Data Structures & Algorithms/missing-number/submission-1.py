class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        full = 0
        miss = 0
        zero = 0
        maxn = 0
        for n in nums:
            miss ^= n
            if n == 0:
                zero = 1
            maxn = max(maxn, n)

        for i in range(maxn + 1):
            full ^= i

        if full == miss:
            if zero:
                return maxn + 1
            else:
                return zero
        return full ^ miss