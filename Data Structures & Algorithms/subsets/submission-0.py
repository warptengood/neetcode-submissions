class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mask = 1 << len(nums)
        result = []
        for i in range(mask):
            subset = []
            for j in range(len(nums)):
                if (i >> j) & 1:
                     subset.append(nums[j])
            result.append(subset)
        return result