import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        def dfs(l, r):
            if (l, r) in mem:
                return mem[(l, r)]
            
            if l >= r:
                return 0
            
            if colors[l] != colors[r]:
                return r - l
                
            lr = dfs(l + 1, r)
            rr = dfs(l, r - 1)
            mem[(l, r)] = max(lr, rr)
            return mem[(l, r)]
    
        mem = {}
        ret = dfs(0, len(colors) - 1)
        return ret


stime = time.time()
print(3 == Solution().maxDistance([1,1,1,6,1,1,1]))
print('elapse time: {} sec'.format(time.time() - stime))
