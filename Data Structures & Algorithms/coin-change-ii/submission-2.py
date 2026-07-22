class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount + 1
        
        dp = [[0] * m for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][amount] = 1

        for i in range(n - 1, -1, -1):
            for j in range(amount, -1, -1):
                dp[i][j] = (0 if j + coins[i] > amount else dp[i][j + coins[i]]) + dp[i + 1][j]

        return dp[0][0]
        # dp = [[-1] * m for _ in range(n+1)]
        # def rec(i, j):
        #     if i >= n:
        #         return j == amount
        #     if j == amount:
        #         return 1
        #     if j > amount:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     dp[i][j] = rec(i, j + coins[i]) + rec(i + 1, j)
        #     return dp[i][j]

        # return rec(0, 0)