class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        p = [0] * n
        p[n - 1] = 1
        res = True

        for i in range(n - 2, -1, -1):
            r = min(i + nums[i], n - 1)
            pref_sum = p[i + 1] - (0 if r == n - 1 else p[r + 1])
            res = (pref_sum > 0)
            p[i] = int(res) + p[i + 1]

        return res