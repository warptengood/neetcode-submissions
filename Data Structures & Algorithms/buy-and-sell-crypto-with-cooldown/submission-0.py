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
            for j in range(i + 1, n):
                val = max(val, dp[j + 2])
            dp[i] = max(dp[i], val - prices[i])
            dp[i] += (0 if i < 2 else prices[i - 2])

        # def rec(day):
        #     if day >= n:
        #         return 0
        #     if dp[day] != INF:
        #         return dp[day]

        #     dp[day] = rec(day + 1)
        #     for i in range(day + 1, n):
        #         dp[day] = max(dp[day], rec(i + 2) + prices[i] - prices[day])
        #     return dp[day]
        
        return dp[0]