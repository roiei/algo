import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findMinDifference(self, timePoints: [str]) -> int:
        mins = []
        for tp in timePoints:
            hour, minute = map(int, tp.split(':'))
            mins += hour*60 + minute,
        mins = sorted(mins)
        mins += 24*60 + mins[0],
        diffs = []
        for i in range(1, len(mins)):
            diffs += mins[i] - mins[i-1],
        return min(diffs)

    def findMinDifference(self, timePoints: [str]) -> int:
        mins = []
        for tp in timePoints:
            hour, minute = map(int, tp.split(':'))
            mins += hour*60 + minute,
        mins = sorted(mins, reverse=True)
        mins.insert(0, 24*60 + mins[-1])
        print(mins)
        diffs = []
        for i in range(1, len(mins)):
            diffs += mins[i-1] - mins[i],
        return min(diffs)




stime = time.time()
print(0 == Solution().findMinDifference(["00:00","23:59","00:00"]))
print('elapse time: {} sec'.format(time.time() - stime))