import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        q = []
        heapq.heappush(q, -a)
        heapq.heappush(q, -b)
        heapq.heappush(q, -c)
        cnt = 0
        
        while True:
            val1 = heapq.heappop(q)
            val2 = heapq.heappop(q)
            if val1 == 0 or val2 == 0:
                break
            
            heapq.heappush(q, val2 + 1)
            
            cnt += 1
        
        return cnt


#assert(True == Solution().check([3,4,5,1,2]))