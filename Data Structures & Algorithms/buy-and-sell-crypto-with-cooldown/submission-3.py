class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = -int(2e9)
        dp = [INF] * (n + 2)
        
        dp[n] = 0 if n < 2 else prices[n - 2]
        dp[n + 1] = 0 if n < 1 else prices[n - 1]
        
        max_val = INF
        can1, can2 = dp[n], dp[n + 1]

        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] - (0 if i < 1 else prices[i - 1])
            dp[i] = max(dp[i], max_val - prices[i])
            dp[i] += (0 if i < 2 else prices[i - 2])
            max_val = max(can2, max_val)
            can2 = can1
            can1 = dp[i]
        return dp[0]