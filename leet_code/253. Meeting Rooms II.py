import collections


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
        mx = 0
        pos = collections.defaultdict(int)
        for interval in intervals:
            pos[interval.start] += 1
            pos[interval.end] -= 1

        pos = sorted(pos.items())

        cnt = 0
        for pos, unit in pos:
            cnt += unit
            mx = max(mx, cnt)

        return mx


def get_intervals(arr):
    ret = []
    for start, end in arr:
        ret += Interval(start, end),
    return ret


#print(2 == Solution().canAttendMeetings(get_intervals([(0,30),(5,10),(15,20)])))
#print(1 == Solution().canAttendMeetings(get_intervals([(2, 7)])))
print(3 == Solution().canAttendMeetings(get_intervals([(6,15),(13,20),(6,17)])))

