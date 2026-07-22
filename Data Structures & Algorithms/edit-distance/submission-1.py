class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        INF = int(1e9)
        dp = [[INF] * m for _ in range(n)]
        def rec(i, j):
            if j == m:
                return n - i
            if i == n:
                return m - j
            if dp[i][j] != INF:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = min(dp[i][j], rec(i + 1, j + 1))
            else:
                # Insert
                dp[i][j] = min(dp[i][j], rec(i, j + 1) + 1)
                # Delete
                dp[i][j] = min(dp[i][j], rec(i + 1, j) + 1)
                # Replace
                dp[i][j] = min(dp[i][j], rec(i + 1, j + 1) + 1)

            return dp[i][j]
        return rec(0, 0)