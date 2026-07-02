class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = [None] * len(prices)
        cur_max = -int(2e9)
        for i in range(len(prices) - 1, -1, -1):
            max_val[i] = cur_max
            cur_max = max(cur_max, prices[i])
        cur_res = 0
        print(max_val)
        for i in range(len(prices)):
            cur_res = max(cur_res, max_val[i] - prices[i])
        return cur_res