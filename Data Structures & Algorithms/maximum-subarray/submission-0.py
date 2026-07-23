class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pref_sum = sum(nums)
        cur_max = pref_sum
        res = -int(2e9)
        for i in range(len(nums) -1, -1, -1):
            cur_max = max(cur_max, pref_sum)
            pref_sum -= nums[i]
            res = max(res, cur_max - pref_sum)
        return res