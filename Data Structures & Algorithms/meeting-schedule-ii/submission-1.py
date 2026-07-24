class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        cnt = 0
        ind = {}
        times = []
        for i in intervals:        
            times.append(i.start)
            times.append(i.end)
        times.append(int(1e9))
        times.sort()
        for t in times:
            if t not in ind:
                ind[t] = cnt
                cnt += 1
        p = [0] * cnt
        for i in intervals:
            p[ind[i.start]] += 1
            p[ind[i.end]] -= 1

        for i in range(1, cnt):
            p[i] += p[i - 1]

        return max(p)