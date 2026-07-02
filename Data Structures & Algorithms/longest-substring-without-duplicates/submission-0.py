class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 0
        cnt = {c:0 for c in s}
        res = 0
        while r < len(s):
            cnt[s[r]] += 1
            while cnt[s[r]] > 1:
                cnt[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res
        
                