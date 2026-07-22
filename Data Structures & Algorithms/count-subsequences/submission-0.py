class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[-1] * m for _ in range(n)]
        def rec(i, j):
            if j == m:
                return 1
            if i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = rec(i + 1, j)
            if s[i] == t[j]:
                dp[i][j] += rec(i + 1, j + 1)
            return dp[i][j]
        
        return rec(0, 0)