class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        def rec(mask):
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for i in range(len(nums)):
                if (mask >> i) & 1 == 0:
                    perm.append(nums[i])
                    rec(mask + (1 << i))
                    perm.pop()
        rec(0)
        return result


