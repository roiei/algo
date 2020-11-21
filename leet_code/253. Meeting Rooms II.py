import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        times = collections.defaultdict(int)
        for interval in intervals:
            times[interval.start] += 1
            times[interval.end] -= 1
        
        times = sorted(times.items(), key=lambda p: p[0])
        cur = 0
        mx = 0
        for time, num in times:
            cur += num
            mx = max(mx, cur)
        
        return mx
            

stime = time.time()
print(2 == Solution().minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
print('elapse time: {} sec'.format(time.time() - stime))