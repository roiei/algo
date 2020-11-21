
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def SubArraySum(self, nums):
        inc = 0
        tot = 0
        
        for i, num in enumerate(nums):
            inc += num*(i + 1)
            tot += inc
        
        return tot

            
stime = time.time()
print(46 == Solution().SubArraySum([3, 1, 2, 4]))
print('elapse time: {} sec'.format(time.time() - stime))