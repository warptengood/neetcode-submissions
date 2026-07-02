class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t:
                result[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((t, i))
        while len(stack) > 0:
            result[stack[-1][1]] = 0
            stack.pop()
        return result