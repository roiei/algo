class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __lt__(self, other):
        if self.start < other.start:
            return True
        return False
    
class Solution:
    def merge(self, intervals):
        n = len(intervals)
        if 1 == n:
            return intervals

        intervals.sort()
        merge = []
        for i in range(n-1):
            if intervals[i].end >= intervals[i+1].start:
                intervals[i+1].start = min(intervals[i].start, intervals[i+1].start)
                intervals[i+1].end = max(intervals[i].end, intervals[i+1].end)
                intervals[i].start = -1
                intervals[i].end = -1

        out = []
        mask = []
        for i in range(len(intervals)):
            idx = '{},{}'.format(intervals[i].start, intervals[i].end)
            if -1 == intervals[i].start and -1 == intervals[i].end:
                continue
            if idx not in mask:
                mask.append(idx)
                out.append(intervals[i])

        return out