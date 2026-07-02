class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromleft = [1]
        for i in range(1, len(nums)):
            fromleft.append(fromleft[-1] * nums[i-1])
        fromright = [1]
        for i in range(len(nums) - 2, -1, -1):
            fromright.append(fromright[-1] * nums[i+1])
        fromright = fromright[::-1]
        return [fromleft[i] * fromright[i] for i in range(len(nums))]


