import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        def dfs(l, r, tot):
            if l > r:
                return 0
            
            if -1 != mem[l][r]:
                return mem[l][r]
            
            ls = tot - stones[r] - dfs(l, r - 1, tot - stones[r])
            rs = tot - stones[l] - dfs(l + 1, r, tot - stones[l])
            
            mem[l][r] = max(ls, rs)
            return max(ls, rs)

        mem = [[-1]*len(stones) for _ in range(len(stones))]
        res = dfs(0, len(stones) - 1, sum(stones))
        return res


stime = time.time()
print(6 == Solution().stoneGameVII([5,3,1,4,2]))
print('elapse time: {} sec'.format(time.time() - stime))
