
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findRightInterval(self, intervals: [[int]]) -> [int]:

        def bisect(vals, target):
            l = 0
            r = len(vals) - 1

            while l <= r:
                m = (l + r)//2
                if vals[m][1] == target: # [m][1] == start, target == end
                    return vals[m][0]    # start's index

                if vals[m][1] > target:
                    r = m - 1
                else:
                    l = m + 1

            return vals[l][0] if l < len(vals) else l

        starts = sorted([(i, item[0]) for i, item in enumerate(intervals)], key=lambda p: p[1])
        n = len(intervals)
        res = [-1]*n

        for i, item in enumerate(intervals):
            start, end = item
            idx = bisect(starts, end)
            if idx < n:
                res[i] = idx

        return res


stime = time.time()
print([-1, 0, 1] == Solution().findRightInterval([ [3,4], [2,3], [1,2] ]))
print([-1, 2, -1] == Solution().findRightInterval([ [1,4], [2,3], [3,4] ]))
print([3,3,3,4,5,-1] == Solution().findRightInterval([[1,12],[2,9],[3,10],[13,14],[15,16],[16,17]]))
print([-1,0,1] == Solution().findRightInterval([[4,5],[2,3],[1,2]]))

print('elapse time: {} sec'.format(time.time() - stime))