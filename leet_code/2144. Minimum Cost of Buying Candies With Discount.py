
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        i = 0
        n = len(cost)
        mn = 0
        
        while i < n:
            num_buy = i + 2
            while i < n and i < num_buy:
                mn += cost[i]
                i += 1
            
            i += 1
        
        return mn


stime = time.time()
print(23 == Solution().minimumCost(cost = [6,5,7,9,2,2]))
print('elapse time: {} sec'.format(time.time() - stime))
