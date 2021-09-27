
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


# the same as "1235. Maximum Profit in Job Scheduling"


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        for i in range(len(rides)):
            rides[i][2] = rides[i][1] - rides[i][0] + rides[i][2]
        
        rides.sort(key=lambda p: p[1])
        dp = [[0, 0]]
        
        for start, end, profit in rides:
            idx = bisect.bisect_left(dp, [start + 1])
            if dp[-1][1] < dp[idx - 1][1] + profit:
                dp += [end, dp[idx - 1][1] + profit],
        
        return dp[-1][1]


stime = time.time()
print(20 == Solution().maxTaxiEarnings(n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]))
print('elapse time: {} sec'.format(time.time() - stime))