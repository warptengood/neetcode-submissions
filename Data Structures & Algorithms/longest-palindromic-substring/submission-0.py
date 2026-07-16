class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp_odd = [[False] * n for _ in range(n)]
        dp_even = [[False] * n for _ in range(n)]

        for i in range(n):
            dp_odd[i][0] = True
            dp_even[i][0] = (i + 1 < n and s[i] == s[i+1])

        for i in range(n):
            for j in range(1, min(i + 1, n - i)):
                dp_odd[i][j] = dp_odd[i][j - 1] & (s[i-j] == s[i+j])

        for i in range(n - 1):
            for j in range(1, min(i + 1, n - i - 1)):
                dp_even[i][j] = dp_even[i][j - 1] & (s[i-j] == s[i+j+1])

        max_val = 0
        max_str = (-1, -1, False) # is_odd
        for i in range(n):
            for j in range(n):
                if dp_even[i][j] and max_val < j * 2 + 2:
                    max_val = j * 2 + 2
                    max_str = i, j, False
                if dp_odd[i][j] and max_val < j * 2 + 1:
                    max_val = j * 2 + 1
                    max_str = i, j, True

        if max_str[2]:
            return s[max_str[0]-max_str[1]:max_str[0]+max_str[1]+1]
        else:
            return s[max_str[0]-max_str[1]:max_str[0]+max_str[1]+2]