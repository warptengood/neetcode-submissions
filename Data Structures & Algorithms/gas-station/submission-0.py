class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        l, r = 0, -1
        cur_cost = 0
        while r < 2 * n and r - l + 1 < n:
            r += 1
            cur_cost += (gas[r % n] - cost[r % n])
            while cur_cost < 0 and l <= r:
                cur_cost -= (gas[l % n] - cost[l % n])
                l += 1

        if r - l + 1 == n:
            return l % n
        return -1