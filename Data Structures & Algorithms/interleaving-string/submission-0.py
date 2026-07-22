class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        if n + m != len(s3):
            return False

        def rec(i, j):
            if i == n and j == m:
                return True
            if dp[i][j] != -1:
                return dp[i][j]
            
            k = i + j
            dp[i][j] = False
            if i < n and s1[i] == s3[k]:
                dp[i][j] |= rec(i + 1, j)
            if j < m and s2[j] == s3[k]:
                dp[i][j] |= rec(i, j + 1)

            return dp[i][j]
        return rec(0, 0)