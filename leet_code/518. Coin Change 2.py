import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def change(self, amount, coins):
        dp = [0]*(amount + 1)
        dp[0] = 1
        for i in coins:
            for j in range(amount+1):
                if j >= i:
                    dp[j] += dp[j-i]
            print(dp)
        print(dp)
        return dp[-1]


stime = time.time()
print(Solution().change(5, [1, 2, 5]))
print('elapse time: {} sec'.format(time.time() - stime))