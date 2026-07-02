class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        res = sorted([(k, v) for k, v in freq.items()], key=lambda p: p[1], reverse=True)
        return [r[0] for r in res][:k]