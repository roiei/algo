
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [i for i in range(n)]
        dp += [0]*7
       
        for i in range(7, n+1):
            dp[i] = max(dp[i-2]*2, dp[i-3]*3)

        return dp[n]
    
    def integerBreak(self, n: int) -> int:
        def dfs(n, inc):
            if (n, inc) in mem:
                return mem[(n, inc)]

            if n <= 3:
                if n == 0:
                    n = 1
                return n*inc

            mem[(n, inc)] = max(dfs(n - 2, inc*2), dfs(n - 3, inc*3))
            return mem[(n, inc)]

        if n == 2 or n == 3:
            return n - 1
        
        mem = {}
        res = dfs(n, 1)
        return res


stime = time.time()
print(36 == Solution().integerBreak(10))
print('elapse time: {} sec'.format(time.time() - stime))

