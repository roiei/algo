
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dfs(piles, turn, l, r, alex, lee):
            if (l, r) in mem:
                return mem[(l, r)]
            
            if l > r:
                return alex > lee
            
            res = []
            if turn:
                res += dfs(piles, not turn, l + 1, r, alex + piles[l], lee),
                res += dfs(piles, not turn, l, r - 1, alex + piles[r], lee),
            else:
                res += dfs(piles, not turn, l + 1, r, alex, lee + piles[l]),
                res += dfs(piles, not turn, l, r - 1, alex, lee + piles[r]),
            
            mem[(l, r)] = any(res)
            return mem[(l, r)]
    
        mem = {}
        return dfs(piles, True, 0, len(piles) - 1, 0, 0)
                


stime = time.time()
#print([0,1,1,1,1,0] == Solution().maxDepthAfterSplit("(()())"))
print([0,0,0,1,1,0,1,1] == Solution().maxDepthAfterSplit("()(())()"))
print('elapse time: {} sec'.format(time.time() - stime))