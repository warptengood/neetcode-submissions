class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        nums = [(v, i) for i, v in enumerate(nums)]
        nums.sort()
        while l <= r:
            if nums[l][0] + nums[r][0] == target:
                return sorted([nums[l][1], nums[r][1]])
            if nums[l][0] + nums[r][0] > target:
                r -= 1
            elif nums[l][0] + nums[r][0] < target:
                l += 1