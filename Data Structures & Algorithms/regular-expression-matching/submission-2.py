class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[-1] * m for _ in range(n)]
        def rec(i, j):
            if i == n:
                if j == m:
                    return True
                else:
                    return j == m - 2 and p[j + 1] == "*"
            if j == m:
                return False
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = False

            if j + 1 < m and p[j + 1] == "*":
                dp[i][j] = rec(i, j + 2)
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] |= rec(i + 1, j)
            else:
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = rec(i + 1, j + 1)
            return dp[i][j]
        return rec(0, 0)