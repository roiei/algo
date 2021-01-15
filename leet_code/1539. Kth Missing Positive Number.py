
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
from typing import List
import bisect


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        i = 1
        
        while i < max(arr) + 2 or cnt != k:
            if i not in arr:
                cnt += 1
            
            if cnt == k:
                return i
        
            i += 1
        
        return -1

    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        
        while k:
            if i in arr:
                i += 1
                continue
            
            k -= 1
            if k == 0:
                return i
            i += 1
            
        return 0

stime = time.time()
print(9 == Solution().findKthPositive([2,3,4,7,11], 5))
print('elapse time: {} sec'.format(time.time() - stime))