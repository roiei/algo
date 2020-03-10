import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def jump(start, n, steps):
            if start in cache:
                return cache[start]
            if start >= n:
                return 1
            cnt = 0
            if start < n:
                cnt += jump(start+1, n, steps+1)
            if start < n-1:
                cnt += jump(start+2, n, steps+2)
            cache[start] = cnt
            return cnt

        cnt = jump(0, n, 0)
        return cnt

    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in [1, 2]:
                if j <= n:
                    dp[i] += dp[i-j]
        return dp[-1]


stime = time.time()
print(3 == Solution().climbStairs(3))
print('elapse time: {} sec'.format(time.time() - stime))