import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0;
        r = x;
        
        while l <= r:
            m = (l + r)//2

            if m**2 == x:
                return m
            elif m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
            
        return l - 1


stime = time.time()
print(2 == Solution().mySqrt(8))
print('elapse time: {} sec'.format(time.time() - stime))
