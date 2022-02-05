import time
from util.util_list import *
from util.util_tree import *
import bisect
import copy
import collections
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        cur = original
        nums = set(nums)
        
        while True:
            if cur not in nums:
                break
            
            cur *= 2
        
        return cur


stime = time.time()
print(24 == Solution().findFinalValue(nums = [5,3,6,1,12], original = 3))
print('elapse time: {} sec'.format(time.time() - stime))