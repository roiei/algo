import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mdiff = -1
        stk = []
        
        for num in nums[::-1]:
            if not stk:
                stk += num,
                continue
            
            while stk and stk[-1] < num:
                stk.pop()
            
            stk += num,
            
            if len(stk) > 1 and stk[0] > stk[-1]:
                mdiff = max(mdiff, stk[0] - stk[-1])
        
        return mdiff


stime = time.time()
print(4 == Solution().maximumDifference(nums = [7,1,5,4]))
print('elapse time: {} sec'.format(time.time() - stime))