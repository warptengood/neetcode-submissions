class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cnt = {}
        for n in nums:
            if n not in cnt:
                cnt[n] = 0
            cnt[n] += 1

        a = [(k, v) for k, v in cnt.items()]

        result = []
        subset = []

        def rec(cur_i, change):
            if change:
                result.append(subset.copy())
            if cur_i == len(a):
                return
            for i in range(a[cur_i][1] + 1):
                subset.extend([a[cur_i][0]] * i)
                rec(cur_i + 1, i != 0)
                for _ in range(i):
                    subset.pop()
        rec(0, True)
        return result