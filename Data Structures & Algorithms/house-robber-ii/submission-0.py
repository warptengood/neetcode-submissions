class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = [[0, 0] for _ in range(n)]
        dp1 = [[0, 0] for _ in range(n)]
        
        dp1[0][1] = nums[0]
        
        for i in range(1, n):
            if i == n - 1:
                dp0[i][0] = max(dp0[i-1][0], dp0[i-1][1])
                dp0[i][1] = dp0[i-1][0] + nums[i]

                dp1[i][0] = max(dp1[i-1][0], dp1[i-1][1])
                dp1[i][1] = max(dp1[i-1][0], dp1[i-1][1])
            else:
                dp0[i][0] = max(dp0[i-1][0], dp0[i-1][1])
                dp0[i][1] = dp0[i-1][0] + nums[i]

                dp1[i][0] = max(dp1[i-1][0], dp1[i-1][1])
                dp1[i][1] = dp1[i-1][0] + nums[i]
        
        return max(dp0[n-1][0], dp0[n-1][1], dp1[n-1][0], dp1[n-1][1])