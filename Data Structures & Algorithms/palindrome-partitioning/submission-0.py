class Solution:
    def check(self, s):
        for i in range((len(s) >> 1) + (len(s) % 2 != 0)):
            if s[i] != s[-i-1]:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        result = []
        substr = []
        def rec(l, r):
            if l == len(s) and r == len(s):
                result.append(substr.copy())
                return
            cur_s = s[l:r+1]
            if self.check(cur_s):
                substr.append(cur_s)
                rec(r+1, r+1)
                substr.pop()
            if r < len(s) - 1:
                rec(l, r + 1)
        rec(0, 0) 
        return result