
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache



class Solution: 
    def numEquivDominoPairs(self, dominoes: [[int]]) -> int:
        d = collections.defaultdict(int)
        
        for domino in dominoes:
            domino.sort()
            d[tuple(domino)] += 1

        vals = [v for k, v in d.items() if v > 1]
        tot = 0

        for val in vals:
            tot += val*(val - 1)//2

        return tot

"""
0 0 0 0 0 -> 4 + 3 + 2 + 1 = 10
0 0 0 0   -> 3 + 2 + 1 = 6
0 0 0     -> 2 + 1 = 3
0 0       -> 1 = 1
"""

stime = time.time()
print(4 == Solution().numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]))
print(3 == Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
print('elapse time: {} sec'.format(time.time() - stime))
