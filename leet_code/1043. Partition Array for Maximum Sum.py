
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def maxSumAfterPartitioning(self, A: [int], K: int) -> int:
        n = len(A)
        dp = [0]*(n + 1)

        for i in range(1, n + 1):
            num = float('-inf')

            print(f'i = {i}, 1, {min(i, K) + 1}')
            for j in range(1, min(i, K) + 1):

                num = max(num, A[i - j])

                print('j = {}, num = {}'.format(j, num))

                dp[i] = max(dp[i], dp[i - j] + num*j)
                print(dp)
            print()

        return dp[n]


stime = time.time()
print(84 == Solution().maxSumAfterPartitioning(A = [1,15,7,9,2,5,10], K = 3))
print('elapse time: {} sec'.format(time.time() - stime))