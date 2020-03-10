
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def maximizeSweetness(self, sweetness: [int], K: int) -> int:
        l, r = 1, sum(sweetness) // (K + 1)
        
        while l < r:
            m = (l + r + 1) // 2
            cur = cuts = 0
            for a in sweetness:
                cur += a
                if cur >= m:
                    cuts += 1
                    cur = 0
                    
            if cuts > K:
                l = m
            else:
                r = m - 1

        return r
    

stime = time.time()
print(6 == Solution().maximizeSweetness([1,2,3,4,5,6,7,8,9], K = 5))
#print(1 == Solution().maximizeSweetness([5,6,7,8,9,1,2,3,4], K = 8))
print('elapse time: {} sec'.format(time.time() - stime))