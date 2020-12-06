import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        inc = 0
        
        while i < len(prices):
            while i + 1 < len(prices) and prices[i] >= prices[i + 1]:
                i += 1
            
            buy = i
            
            while i + 1 < len(prices) and prices[i] < prices[i + 1]:
                i += 1
            
            sel = i
            
            if sel > buy:
                inc += prices[sel] - prices[buy]
            
            i += 1
        
        return inc

    def maxProfit(self, prices: List[int]) -> int:


stime = time.time()
print(7 == Solution().maxProfit([7,1,5,3,6,4]))
print(4 == Solution().maxProfit([1,2,3,4,5]))
print('elapse time: {} sec'.format(time.time() - stime))
