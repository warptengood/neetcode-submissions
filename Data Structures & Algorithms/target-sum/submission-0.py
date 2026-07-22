class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, m = len(nums), target + 1
        dp = {}
        def rec(i, j):
            if i == n:
                return j == target
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = 0

            dp[(i, j)] = rec(i + 1, j + nums[i]) + rec(i + 1, j - nums[i])
            return dp[(i, j)]
        return rec(0, 0)