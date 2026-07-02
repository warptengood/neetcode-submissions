class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ('+', '-', '*', '/'):
                second = stack.pop()
                first = stack.pop()
                if t == '+':
                    stack.append(first + second)
                elif t == '-':
                    stack.append(first - second)
                elif t == '*':
                    stack.append(first * second)
                elif t == '/':
                    f_m = -1 if first < 0 else 1
                    s_m = -1 if second < 0 else 1 
                    stack.append((f_m * s_m)*(abs(first) // abs(second)))
            else:
                stack.append(int(t))
        return stack[-1]