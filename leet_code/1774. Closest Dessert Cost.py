import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n = len(toppingCosts)
        
        def dfs(sel, start, kinds):
            if start == n:
                kinds.add(sum(sel))
                return
            
            kinds.add(sum(sel))

            for i in range(start, n):
                dfs(sel + [toppingCosts[i], toppingCosts[i]], i + 1, kinds)
                dfs(sel + [toppingCosts[i]], i + 1, kinds)
        
        
        mn = float('inf')
        mn_val = []

        for base in baseCosts:
            kinds = {base}
            dfs([base], 0, kinds)
            for kind in kinds:

                if mn > abs(kind - target):
                    mn = abs(kind - target)
                    mn_val = [kind]
                elif mn == abs(kind - target):
                    mn_val += kind,

        return sorted(mn_val)[0]



stime = time.time()
# print(10 == Solution().closestCost(baseCosts = [1,7], toppingCosts = [3,4], target = 10))
# print(17 == Solution().closestCost(baseCosts = [2,3], toppingCosts = [4,5,100], target = 18))
# print(8 == Solution().closestCost(baseCosts = [3,10], toppingCosts = [2,5], target = 9))
# print(10 == Solution().closestCost(baseCosts = [10], toppingCosts = [1], target = 1))
print(6345 == Solution().closestCost([5020,1159], [1253,5085,4881,2593], 6819))
print('elapse time: {} sec'.format(time.time() - stime))