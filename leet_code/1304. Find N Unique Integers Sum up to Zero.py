
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
import heapq


class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        odd = n%2
        res = []
        
        for i in range(1, n//2 + 1):
            res += i,
            res += -i,
        
        if odd:
            res += 0,
        
        return res


stime = time.time()
print([-7,-1,1,3,4] == Solution().sumZero(n = 5))
print('elapse time: {} sec'.format(time.time() - stime))