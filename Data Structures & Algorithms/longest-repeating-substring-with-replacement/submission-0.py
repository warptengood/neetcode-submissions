class Solution:

    def check(self, cnt, k):
        present = sorted(list(cnt.values()))
        if len(present) == 0:
            return True
        return sum(present[:-1]) <= k

    def characterReplacement(self, s: str, k: int) -> int:
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cnt = {a: 0 for a in alpha}

        l, r = 0, 0
        res = 1
            

        while r < len(s):
            cnt[s[r]] += 1

            while not self.check(cnt, k):
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
            r += 1
        return res
