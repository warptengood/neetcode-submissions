class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = 0-int(2e9)
        dp = [INF] * (n + 2)
        
        dp[n] = 0 if n < 2 else prices[n - 2]
        dp[n + 1] = 0 if n < 1 else prices[n - 1]

        for i in range(n - 1, -1, -1):

            dp[i] = dp[i + 1] - (0 if i < 1 else prices[i - 1])
            val = dp[i]
            for j in range(i + 3, n+2):
                val = max(val, dp[j])
            dp[i] = max(dp[i], val - prices[i])
            dp[i] += (0 if i < 2 else prices[i - 2])

        return dp[0]