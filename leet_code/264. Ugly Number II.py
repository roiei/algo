import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def nthUglyNumber(self, n:int) -> int:
        q = [1]
        i = 0
        
        while i < n:
            cur = heapq.heappop(q)
            
            for factor in [2, 3, 5]:
                val = cur*factor
                if val in q:
                    continue
                heapq.heappush(q, val)
            
            i += 1
            
        return cur


stime = time.time()
print(12 == Solution().nthUglyNumber(10))
print('elapse time: {} sec'.format(time.time() - stime))