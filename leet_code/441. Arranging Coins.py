
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        
        tot = 1
        cnt = 1
        step = 2
        
        while tot + step <= n:
            tot += step
            step += 1
            cnt += 1
        
        return cnt

    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return n
        
        l = 0
        r = n
        
        while l <= r:
            m = (l + r)//2
            
            area = m*(m - 1)//2
            
            if area <= n < (m + 1)*m//2:
                return m - 1
            
            if area > n:
                r = m - 1
            else:
                l = m + 1
        
        return l - 1


stime = time.time()
print(2 == Solution().arrangeCoins(5))
print(3 == Solution().arrangeCoins(8))
print('elapse time: {} sec'.format(time.time() - stime))