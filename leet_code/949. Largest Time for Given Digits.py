import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def largestTimeFromDigits(self, A: [int]) -> str:
        max_hour = -1
        max_min = -1
        mval = -1
        
        def perm(nums, n, skip, depth, trace, res):
            nonlocal max_hour, max_min
            nonlocal mval
            if depth == n:
                hour = int(''.join([str(val) for val in trace[:2]]))
                minute = int(''.join([str(val) for val in trace[2:]]))
                if (0 <= hour <= 23 and 0 <= minute <= 59):
                    cur = hour*60+minute
                    if mval < cur:
                        mval = cur
                        max_hour = hour
                        max_min = minute
                return
            for i in range(n):
                if skip[i] == True:
                    continue
                skip[i] = True
                trace += nums[i],
                perm(nums, n, skip, depth+1, trace, res)
                trace.pop()
                skip[i] = False
        
        skip = [False]*len(A)
        perm(A, len(A), skip, 0, [])
        if mval == -1:
            return ""
        return '{:02}:{:02}'.format(max_hour, max_min)


stime = time.time()
print("20:40" == Solution().largestTimeFromDigits([2,0,0,4]))
print('elapse time: {} sec'.format(time.time() - stime))

