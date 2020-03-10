
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
            
            
stime = time.time()

print(2 == Solution().removeCoveredIntervals([[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]))
#print(2 == Solution().removeCoveredIntervals([[1,4],[3,6],[2,8]]))
print('elapse time: {} sec'.format(time.time() - stime))