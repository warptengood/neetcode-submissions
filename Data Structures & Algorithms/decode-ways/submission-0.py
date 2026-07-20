class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [[-1, -1] for _ in range(n)]
        # print(dp)
        def rec(cur_i, will_merge):
            if dp[cur_i][will_merge] != -1:
                return dp[cur_i][will_merge]
            # print(cur_i, will_merge)

            dp[cur_i][will_merge] = 0
            if will_merge:
                if s[cur_i - 1] == '1' and 0 <= int(s[cur_i]) <= 9:
                    dp[cur_i][will_merge] = 1 if cur_i == n - 1 else rec(cur_i+1, 0)
                elif s[cur_i - 1] == '2' and 0 <= int(s[cur_i]) <= 6:
                    dp[cur_i][will_merge] = 1 if cur_i == n - 1 else rec(cur_i+1, 0)
            else:
                if s[cur_i] != '0':
                    dp[cur_i][will_merge] = 1 if cur_i == n - 1 else rec(cur_i+1, 0) + rec(cur_i+1, 1)
            return dp[cur_i][will_merge]
        return rec(0, 0)