class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[-1] * m for _ in range(n)]

        def rec(x, y):
            if x == n or y == m:
                return 0
            if dp[x][y] != -1:
                return dp[x][y]
            

            case1 = rec(x + 1, y + 1)
            case2 = rec(x, y + 1)
            case3 = rec(x + 1, y)

            dp[x][y] = max(case1 + (text1[x] == text2[y]), case2, case3)
            return dp[x][y]
        
        return rec(0, 0)