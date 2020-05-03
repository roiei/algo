
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def numOfWays(self, n: int) -> int:
        f = g = pf = pg = 6
        
        for i in range(n - 1):
            f = 2*pf + 2*pg
            g = 2*pf + 3*pg
            pf = f
            pg = g
        
        return (f + g)%(10**9 + 7)


stime = time.time()
print(12 == Solution().numOfWays(1))
print('elapse time: {} sec'.format(time.time() - stime))