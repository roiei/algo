
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
        if not ops:
            return m*n

        minm = sorted(ops, key=lambda p: p[0])[0][0]
        minn = sorted(ops, key=lambda p: p[1])[0][1]
        
        return minm*minn
        

        


stime = time.time()
print(4 == Solution().maxCount(m = 3, n = 3, operations = [[2,2],[3,3]]))
print('elapse time: {} sec'.format(time.time() - stime))