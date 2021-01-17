import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [-1] + heights + [-1]
        stk = [0]
        mx = 0
        
        for i in range(1, len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                idx = stk.pop()
                mx = max(mx, heights[idx]*(i - stk[-1] - 1))
            
            stk += i,
        return mx


stime = time.time()
print(10 == Solution().largestRectangleArea([2,1,5,6,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))
