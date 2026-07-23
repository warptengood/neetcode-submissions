class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
        while len(left) > 0:
            if len(star) == 0:
                return False
            if star[-1] < left[-1]:
                return False
            left.pop()
            star.pop()
        return True