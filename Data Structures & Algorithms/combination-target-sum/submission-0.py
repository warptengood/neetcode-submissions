class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        cur_elems = []
        def rec(cur_id, cur_sum):
            if cur_sum == target:
                result.append(cur_elems.copy())
                return
            if cur_sum + nums[cur_id] <= target:
                cur_elems.append(nums[cur_id])
                rec(cur_id, cur_sum + nums[cur_id])
                cur_elems.pop()
            if cur_id + 1 < len(nums):
                rec(cur_id + 1, cur_sum)
            
        rec(0, 0)
        return result