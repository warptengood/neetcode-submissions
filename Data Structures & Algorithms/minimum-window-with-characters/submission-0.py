class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ref = {}
        for c in t:
            if c not in ref:
                ref[c] = 0
            ref[c] += 1
        
        cur = {}
        
        min_l, min_r = None, None
        l, r = 0, -1

        def check():
            for k, v in ref.items():
                if k not in cur:
                    return False
                if cur[k] < v:
                    return False
            return True

        while r < len(s):
            while check():
                if min_l is None or min_r - min_l > r - l:
                    min_l = l
                    min_r = r
                cur[s[l]] -= 1
                l += 1
            r += 1
            if r == len(s):
                break
            if s[r] not in cur:
                cur[s[r]] = 0
            cur[s[r]] += 1
        
        if min_l is None:
            return ""
        return s[min_l:min_r+1]