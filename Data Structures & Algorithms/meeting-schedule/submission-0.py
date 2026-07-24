class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: (i.start, i.end))
        if len(intervals) > 0:
            st = intervals[0]
            for i in range(1, len(intervals)):
                if intervals[i].start < st.end:
                    return False
                st = intervals[i]
        return True