import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = []
        
        for i in range(n):
            discount = 0
            for j in range(i + 1, n):
                if prices[i] >= prices[j]:
                    discount = prices[j]
                    break
            
            res += prices[i] - discount,
        
        return res


stime = time.time()
print([4,2,4,2,3] == Solution().finalPrices([8,4,6,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))