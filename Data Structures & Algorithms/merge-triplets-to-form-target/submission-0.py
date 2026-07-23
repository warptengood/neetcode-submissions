class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [-1, -1, -1]
        for tri in triplets:
            score = 0
            for i in range(3):
                if tri[i] > cur[i]:
                    if tri[i] <= target[i]:
                        score += 1
                else:
                    score += 1
                    
            if score == 3:
                cur = [max(a, b) for a, b in zip(cur, tri)]
        return cur == target