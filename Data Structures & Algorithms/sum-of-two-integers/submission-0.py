class Solution:

    def add(self, a, b):
        rem = 0
        res = 0
        for i in range(32):
            if (a >> i) & 1 and (b >> i) & 1:
                res |= (rem << i)
                rem = 1
            elif not ((a >> i) & 1) and not ((b >> i) & 1):
                res |= (rem << i)
                rem = 0
            else:
                res |= ((rem ^ 1) << i)
        return res


    def getSum(self, a: int, b: int) -> int:
        c = self.add(a, b)
        if c & (1 << 31):
            return ~(c ^ 0xFFFFFFFF)
        return c