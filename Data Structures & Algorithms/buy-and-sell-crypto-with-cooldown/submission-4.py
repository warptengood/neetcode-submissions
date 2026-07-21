class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        INF = -int(2e9)
        # dp = [INF] * (n + 2)
        
        res = INF
        res1 = 0 if n < 2 else prices[n - 2]
        res2 = 0 if n < 1 else prices[n - 1]
        
        max_val = INF
        can1, can2 = res1, res2

        for i in range(n - 1, -1, -1):
            res = res1 - (0 if i < 1 else prices[i - 1])
            res = max(res, max_val - prices[i])
            res += (0 if i < 2 else prices[i - 2])
            max_val = max(can2, max_val)
            can2 = can1
            can1 = res

            res2 = res1
            res1 = res

        return res1