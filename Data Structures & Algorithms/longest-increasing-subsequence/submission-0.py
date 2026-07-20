class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        def rec(cur_i):
            if cur_i == n:
                return 0
            if dp[cur_i] != -1:
                return dp[cur_i]
            
            dp[cur_i] = 1
            for i in range(cur_i + 1, n):
                if nums[i] > nums[cur_i]:
                    dp[cur_i] = max(dp[cur_i], rec(i) + 1)
            return dp[cur_i]
        
        ans = 0
        for i in range(0, n):
            ans = max(ans, rec(i))
        return ans