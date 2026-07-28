class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        sign = n >= 0
        n = abs(n)
        while n > 0:
            if n % 2 != 0:
                result = result * x if sign else result / x
            x *= x
            n >>= 1
        return result