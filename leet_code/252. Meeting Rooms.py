class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        #intervals.sort(key=lambda p: (p.start, p.end))
        if not intervals:
            return True

        intervals.sort(key=lambda p: (p.start, p.end))

        cur = intervals.pop()

        while intervals:
            if cur.end > intervals[0].start and cur.start < intervals[0].end:
                return False
            cur = intervals.pop(0)

        return True


def get_intervals(arr):
    ret = []
    for start, end in arr:
        ret += Interval(start, end),
    return ret



print(False == Solution().canAttendMeetings(get_intervals([(0,30),(5,10),(15,20)])))
print(True == Solution().canAttendMeetings(get_intervals([(5,8),(9,15)])))