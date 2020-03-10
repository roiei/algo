
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:        
        res = []
        for i in range(0, len(nums), 2):
            res += nums[i]*[nums[i + 1]]
        return res
        
            
stime = time.time()
print([2,4,4,4] == Solution().decompressRLElist([1,2,3,4]))
print('elapse time: {} sec'.format(time.time() - stime))