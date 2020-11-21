
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        
        idx = collections.defaultdict(int)
        idx[0] = -1
        tot = 0
        res = []
        
        for i, num in enumerate(nums):
            tot += num
            if tot in idx:
                res += (idx[tot] + 1, i),
            elif num == 0:
                res += (i, i),
            
            idx[tot] = i
        
        return res[-1] if res else (0, 0)

            
stime = time.time()
print(Solution().subarraySum([-5,10,5,-3,1,1,1,-2,3,-4]))
print('elapse time: {} sec'.format(time.time() - stime))