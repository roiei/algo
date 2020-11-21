
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
import bisect


class Solution:
    def dominantIndex(self, nums: [int]) -> int:
        q = []
        for i, num in enumerate(nums):
            heapq.heappush(q, (-num, i))
        
        mx, midx = heapq.heappop(q)
        mx *= -1
        while q:
            val, idx = heapq.heappop(q)
            val *= -1
            if mx < val*2:
                return -1
        
        return midx
        

stime = time.time()
print(1 == Solution().dominantIndex([3, 6, 1, 0]))
print('elapse time: {} sec'.format(time.time() - stime))