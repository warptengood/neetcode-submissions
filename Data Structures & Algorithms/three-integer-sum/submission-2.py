class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        occ = {}
        for num in nums:
            if num not in occ:
                occ[num] = 0
            occ[num] += 1
        n = len(nums)
        res = set()

        nums.sort()

        for i in range(n):
            for j in range(i):
                occ[nums[i]] -= 1
                occ[nums[j]] -= 1

                if -(nums[i] + nums[j]) in occ and occ[-(nums[i] + nums[j])] > 0:
                    res.add(tuple(sorted([nums[i], nums[j], -(nums[i] + nums[j])])))
                
                occ[nums[i]] += 1
                occ[nums[j]] += 1
        return list(res)