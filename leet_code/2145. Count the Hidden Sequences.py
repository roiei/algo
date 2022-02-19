
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def numberOfArrays(self, residuals: List[int], low_limit: int, high_limit: int) -> int:
        scope = high_limit - low_limit
        mn = 0
        mx = 0
        inc = 0
        
        for diff in residuals:
            inc += diff
            mn = min(mn, inc)
            mx = max(mx, inc)
        
        in_scope = mx - mn
        
        return scope - in_scope + 1 if scope >= in_scope else 0

    def getNumOfSequences(self, residuals: List[int], low_limit: int, high_limit: int) -> int:
        scope = high_limit - low_limit
        mn = 0
        mx = 0
        inc = 0
        
        for diff in residuals:
            inc += diff
            mn = min(mn, inc)
            mx = max(mx, inc)
        
        in_scope = mx - mn
        
        return scope - in_scope + 1 if scope >= in_scope else 0


stime = time.time()
#print(4 == Solution().numberOfArrays(residuals = [3,-4,5,1,-2], low_limit = -4, high_limit = 5))
print(Solution().numberOfArrays(residuals = [2,3,-6,-2], low_limit = -3, high_limit = 7))
print('elapse time: {} sec'.format(time.time() - stime))
