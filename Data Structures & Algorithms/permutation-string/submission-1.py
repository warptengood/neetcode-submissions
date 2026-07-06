class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        cnt = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
        ref = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}

        for i in range(len(s1)):
            cnt[s2[i]] += 1
            ref[s1[i]] += 1
        
        l, r = 0, len(s1) - 1
        while r < len(s2):
            if cnt == ref:
                return True
            r += 1
            if r == len(s2):
                break
            cnt[s2[r]] += 1
            cnt[s2[l]] -= 1
            l += 1
        return False

        