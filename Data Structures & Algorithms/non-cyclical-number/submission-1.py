class Solution:

    def get(self, n):
        total = 0
        while n != 0:
            total += (n % 10) * (n % 10)
            n //= 10
        return total

    def isHappy(self, n: int) -> bool:
        was = set()
        while n not in was:
            if n == 1:
                return True
            was.add(n)
            n = self.get(n)
        return False