
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tot = 0
        mn = float('inf')

        for num in nums:
            tot += num
            mn = min(mn, tot)
        
        if mn < 0:
            mn = abs(mn) + 1
        else:
            mn = 1
        
        return mn


stime = time.time()
print(5 == Solution().minStartValue([-3,2,-3,4,2]))
print('elapse time: {} sec'.format(time.time() - stime))