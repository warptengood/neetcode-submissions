class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        new = newInterval
        if len(new) == 0:
            new = None
        if len(intervals) == 0:
            return [newInterval]
        for i in intervals:
            if new is not None:
                if (
                    i[0] <= new[0] <= i[1] or i[0] <= new[1] <= i[1] or
                    new[0] <= i[0] <= new[1] or new[0] <= i[1] <= new[1]
                ):
                    result.append([min(i[0], new[0]), max(i[1], new[1])])
                    new = None
                elif new[1] < i[0]:
                    result.append(new)
                    result.append(i)
                    new = None
                else:
                    result.append(i)
            else:
                if len(result) == 0:
                    result.append(i)
                elif result[-1][1] < i[0]:
                    result.append(i)
                else:
                    new_last = result.pop()
                    result.append([min(i[0], new_last[0]), max(i[1], new_last[1])])
        if new is not None:
            result.append(new)
        return result