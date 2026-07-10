
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []
        candidates.sort()
        cnt = {}
        for c in candidates:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
        
        pars = [(k, v) for k, v in cnt.items()]
        
        def rec(id, cur_sum):
            if cur_sum == target:
                result.append(subset.copy())
                return
            if id == len(pars):
                return
            
            for i in range(pars[id][1] + 1):
                if cur_sum + i * pars[id][0] <= target:
                    subset.extend([pars[id][0]] * i)
                    rec(id + 1, cur_sum + i * pars[id][0])
                    for _ in range(i):
                        subset.pop()
                else:
                    return
        
        rec(0, 0)
        return result