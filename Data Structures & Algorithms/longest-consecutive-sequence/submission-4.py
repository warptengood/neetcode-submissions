class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        cur = 1
        max_len = 1 if len(nums) > 0 else 0
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                cur += 1
                max_len = max(cur, max_len)
            else:
                cur = 1
        return max_len