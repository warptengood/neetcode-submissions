class Solution:
    def countBits(self, n: int) -> List[int]:
        slots = 0
        temp_n = n
        while temp_n:
            slots += 1
            temp_n >>= 1

        pen = [0] * (1 << slots)
        # print(slots)
        for i in range(2, slots + 1):
            for mask in range(1 << (slots - i)):
                # print(bin((mask << i) + (1 << (i - 1)) - 1)[2:], i - 1)
                pen[(mask << i) + (1 << (i - 1)) - 1] = i - 1
        # for i in range(n + 1):
        #     print(bin(i)[2:], pen[i])
        res = [0]
        for i in range(1, n + 1):
            res.append(res[-1] + 1 - pen[i - 1])
        return res