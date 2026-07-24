class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda i: (i[0], i[1]))
        for i in intervals:
            if len(result) == 0:
                result.append(i)
            else:
                if result[-1][0] <= i[0] <= result[-1][1]:
                    new = result.pop()
                    result.append([min(new[0], i[0]), max(new[1], i[1])])
                else:
                    result.append(i)
        return result