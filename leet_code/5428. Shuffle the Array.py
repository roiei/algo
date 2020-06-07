import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res += nums[i],
            res += nums[i + n],
        
        return res
        

stime = time.time()
print([2,3,5,4,1,7]  == Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))
print('elapse time: {} sec'.format(time.time() - stime))

     