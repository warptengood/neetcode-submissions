class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        n, m = len(num1), len(num2)
        nums = []
        for i in range(n - 1, -1, -1):
            base = [0] * (n - i - 1)
            base.extend([int(num1[i]) * int(num2[j]) for j in range(m - 1, -1, -1)])
            nums.append(base)

        res = [0]
        while len(nums) > 0:
            cur = nums.pop()
            rem = 0
            last_pos = 0
            for i in range(len(cur)):
                if i < len(res):
                    res[i] += cur[i] + rem
                    rem = res[i] // 10
                    res[i] %= 10
                else:
                    res.append(cur[i] + rem)
                    rem = res[-1] // 10
                    res[-1] %= 10
                last_pos = i
            last_pos += 1
            while rem != 0:
                if last_pos < len(res):
                    res[last_pos] += rem
                    rem = res[last_pos] // 10
                    res[last_pos] %= 10
                else:
                    res.append(rem)
                    rem = 0
                last_pos += 1

        res.reverse()
        return ''.join([str(d) for d in res])
        