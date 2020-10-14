
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def removeCoveredIntervals(self, intervals: [[int]]) -> int:
        intervals.sort(key=lambda p: p[0])
        
        while True:
            i = 0
            pn = len(intervals)
            
            while i < len(intervals) - 1:
                s, e = intervals[i]
                ns, ne = intervals[i + 1]
                
                if ns <= s <= e <= ne:
                    intervals.pop(i)
                    continue
                
                if s <= ns <= ne <= e:
                    intervals.pop(i + 1)

                i += 1

            if pn == len(intervals):
                break
        
        return len(intervals)

    def removeCoveredIntervals(self, intervals):
        intervals.sort(key = lambda x: (x[0], -x[1]))
        n = len(intervals)

        s = intervals[0][0]
        e = intervals[0][1]

        intervals.pop(0)
        cnt = 0

        for cs, ce in intervals:
            if s <= cs and ce <= e:
                cnt += 1
            else:
                s, e = cs, ce

        return n - cnt

            
stime = time.time()
print(2 == Solution().removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]))
print(2 == Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print(1 == Solution().removeCoveredIntervals([[1,2],[1,4],[3,4]]))
print('elapse time: {} sec'.format(time.time() - stime))