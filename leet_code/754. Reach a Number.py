import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step = 0
        cur = 0
        
        while True:
            if cur == target:
                break
            
            if cur > target and (cur - target)%2 == 0:
                break
            
            step += 1
            cur += step
        
        return step


stime = time.time()
sol = Solution()
print(3 == sol.reachNumber(2))
print('elapse time: {} sec'.format(time.time() - stime))
