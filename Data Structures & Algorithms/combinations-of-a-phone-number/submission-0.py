phone = [
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        sub = []
        def rec(i):
            if i == len(digits):
                if len(sub) > 0:
                    result.append("".join(sub))
                return
            but = int(digits[i]) - 2
            for c in phone[but]:
                sub.append(c)
                rec(i + 1)
                sub.pop()
        rec(0)
        return result