import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            for j in range(i):
                dp[i] = dp[i] + dp[j]*dp[i-j-1]
        return dp[n]


stime = time.time()
#print(5 == Solution().numTrees(3))
print(Solution().numTrees(5))
print('elapse time: {} sec'.format(time.time() - stime))