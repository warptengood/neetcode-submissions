class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        ngroup = len(hand) // groupSize
        cnt = {}
        heap = []
        for c in hand:
            if c not in cnt:
                cnt[c] = 0
                heapq.heappush(heap, c)
            cnt[c] += 1

        for i in range(ngroup):
            while cnt[heap[0]] == 0 and len(heap) > 0:
                heapq.heappop(heap)

            if len(heap) == 0:
                return False
            
            cur = heap[0]
            for _ in range(groupSize):
                if cur not in cnt or cnt[cur] == 0:
                    return False
                cnt[cur] -= 1
                cur += 1
        
        return True