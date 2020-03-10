import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minCostClimbingStairs_mem(self, cost: [int]) -> int:
        if not cost:
            return 0
        cache = {}
        def dfs(cost, l, r):
            nonlocal cache
            if (l, r) in cache:
                return cache[(l, r)]
            if l > r:
                return 0
            left = dfs(cost, l+1, r)
            right = dfs(cost, l+2, r)
            cache[(l, r)] = cost[l] + min(left, right)
            return cache[(l, r)]
        
        first = dfs(cost, 0, len(cost)-1)
        second = dfs(cost, 1, len(cost)-1)
        return min(first, second)

    def minCostClimbingStairs(self, cost: [int]) -> int:
        if not cost:
            return 0
        n = len(cost)
        dp = [float('inf')]*(n+1)
        dp[0] = 0

        

        for jump in [1, 2, 3]:
            for i in range(jump, n+1):
                dp[i] = min(dp[i], dp[i-jump] + cost[i-jump])

            print(dp)

        return dp[-1]


stime = time.time()
#print(Solution().minCostClimbingStairs([0, 0, 0, 1]))
#print(15 == Solution().minCostClimbingStairs_mem([10, 15, 20]))
print(15 == Solution().minCostClimbingStairs([10, 15, 20]))
print(6 == Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print('elapse time: {} sec'.format(time.time() - stime))