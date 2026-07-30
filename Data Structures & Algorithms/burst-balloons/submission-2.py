class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # def tup(arr):
        #     ans = 0
        #     ans_order = []
        #     for i in range(len(arr)):
        #         order = [arr[i]]
        #         reward = (1 if i == 0 else arr[i - 1]) * arr[i] * (1 if i == len(arr) - 1 else arr[i + 1])
        #         tup_res = tup(arr[:i] + arr[i + 1:])
        #         reward += tup_res[0]
        #         order.extend(tup_res[1])
        #         if ans < reward:
        #             ans = reward
        #             ans_order = order

        #     return ans, ans_order
        # arr = nums.copy()
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        def rec(l, r):
            if dp[l][r] != -1:
                return dp[l][r]
            dp[l][r] = 0
            for i in range(l, r + 1):
                left = rec(l, i - 1)
                right = rec(i + 1, r)
                dp[l][r] = max(dp[l][r], left + right + nums[i] * nums[l - 1] * nums[r + 1])
            return dp[l][r]
        return rec(1, n - 2)