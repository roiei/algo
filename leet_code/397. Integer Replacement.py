import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def integerReplacement(self, n: int) -> int:
        cache = {}
        def op(n):
            if n in cache:
                return cache[n]
            if 1 == n:
                return 0
            res = []
            if 0 == n%2:
                res += 1 + op(n//2),
            else:                
                res += min(1 + op(n+1), 1 + op(n-1)),
            cache[n] = min(res)
            return cache[n]
    
        ret = op(n)
        return ret


stime = time.time()
print(Solution().dailyTemperatures_timeout([73, 74, 75, 71, 69, 72, 76, 73]))
print('elapse time: {} sec'.format(time.time() - stime))