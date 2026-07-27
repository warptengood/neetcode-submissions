class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        res = []
        rem = 1
        for d in digits:
            cur = d + rem
            rem = 0
            if cur > 9:
                rem = cur // 10
                cur %= 10
            res.append(cur)
        if rem != 0:
            res.append(rem)
        res.reverse()
        return res