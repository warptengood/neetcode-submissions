class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanum = "abcdefghijklmnopqrstuvwxyz0123456789"
        s = [c for c in s if c in alphanum]
        n = len(s)
        for i in range(n):
            if s[i] != s[n - i - 1]:
                return False
        return True