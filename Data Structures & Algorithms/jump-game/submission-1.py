class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [0] * n
        p = [0] * n
        dp[n - 1] = 1
        p[n - 1] = 1

        for i in range(n - 2, -1, -1):
            l = i
            r = min(i + nums[i], n - 1)
            pref_sum = p[i + 1] - (0 if r == n - 1 else p[r + 1])
            dp[i] = (pref_sum > 0)
            p[i] = dp[i] + p[i + 1]
            # for j in range(l, r):
            #     dp[i] |= dp[j]

        return bool(dp[0])