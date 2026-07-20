class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        dp = {}
        def rec(cur_i, sum):
            if cur_i == n:
                return total - sum == sum
            if (cur_i, sum) in dp:
                return dp[(cur_i, sum)]
            
            dp[(cur_i, sum)] = rec(cur_i + 1, sum + nums[cur_i]) | rec(cur_i + 1, sum)
            return dp[(cur_i, sum)]
        return rec(0, 0)