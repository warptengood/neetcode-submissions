class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n, m = len(coins), amount + 1
        
        # dp = [[0] * m for _ in range(n+1)]
        
        # for i in range(n + 1):
        #     dp[i][0] = 1
        
        # for i in range(n - 1, -1, -1):
        #     for j in range(1, m):
        #         for k in range(j // coins[i] + 1):
        #             dp[i][j] += dp[i + 1][j - coins[i] * k]
        # return dp[0][amount]
        dp = [[-1] * m for _ in range(n+1)]
        def rec(i, j):
            if i >= n:
                return j == amount
            if j == amount:
                return 1
            if j > amount:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = rec(i, j + coins[i]) + rec(i + 1, j)
            return dp[i][j]

        return rec(0, 0)