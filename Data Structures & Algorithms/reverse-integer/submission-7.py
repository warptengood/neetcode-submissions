class Solution:

    INT_MAX = (1 << 31) - 1
    INT_MIN = -(1 << 31)

    def max_num(self, x):
        maxnum = 1
        while x >= 10:
            x //= 10
            maxnum *= 10
        return maxnum

    def reverse(self, x: int) -> int:
        is_neg = x < 0
        x = abs(x)
        max_pos = self.max_num(x)
        res = 0
        while max_pos:
            if is_neg and -res < self.INT_MIN + (x % 10) * max_pos:
                return 0
            if not is_neg and res > self.INT_MAX - (x % 10) * max_pos:
                return 0
            res += (x % 10) * max_pos
            x //= 10
            max_pos //= 10
        if is_neg:
            res *= -1
        return res