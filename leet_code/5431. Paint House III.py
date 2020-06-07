import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools



class Solution:
    def minCost(self, houses: [int], cost: [[int]], m: int, n: int, target: int) -> int:
        dp, dp2 = {(0, 0): 0}, {}

        for i, a in enumerate(A):
            for cj in (range(1, n + 1) if a == 0 else [a]):
                for ci, b in dp:
                    b2 = b + (ci != cj)
                    if b2 > target:continue
                    dp2[cj, b2] = min(dp2.get((cj,b2), float('inf')), dp[ci, b] + (cost[i][cj - 1] if cj != a else 0))
            dp, dp2 = dp2, {}

        return min([dp[c, b] for c, b in dp if b == target] or [-1])


    def minCost(self, houses: [int], cost: [[int]], m: int, n: int, target: int) -> int:
        def dfs(i, t, clr):
            if (i, t, clr) in mem:
                return mem[(i, t, clr)]

            if i == m:
                return 0 if t == target else float('inf')

            if houses[i] > 0:
                return dfs(i + 1, t + int(houses[i] != clr), houses[i])

            res = []
            for j in range(1, n + 1):
                res += cost[i][j - 1] + dfs(i + 1, t + int(j != clr), j),
            
            mem[(i, t, clr)] = min(float('inf'), min(res))
            return mem[(i, t, clr)]

        mem = {}
        mn = dfs(0, 0, -1)
        return -1 if mn == float('inf') else mn


stime = time.time()
print(9 == Solution().minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
print('elapse time: {} sec'.format(time.time() - stime))

     