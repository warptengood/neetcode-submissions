class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums)-1]:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m
            elif nums[m] > nums[l]:
                l = m
            else:
                return nums[r]

"""
[3,4,5,6,1,2]
[0,1,2,3,4,5]

0,5,2
2,5,3
3,5,4
3,4,3
"""