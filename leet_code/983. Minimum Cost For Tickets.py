import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def mincostTickets(self, days: [int], costs: [int]) -> int:
        mx_day = days[-1]
        dp = [float('inf')]*(mx_day + 1)
        dp[0] = 0

        for cur in range(1, mx_day + 1):
            if cur not in days:
                dp[cur] = dp[cur - 1]

            for cost, day in zip(costs, [1, 7, 30]):
                if cur - day < 0:
                    dp[cur] = min(dp[cur], cost)
                    continue

                dp[cur] = min(dp[cur], dp[cur - day] + cost)

        return dp[-1]
                    

# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.


stime = time.time()
#print(11 == Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
print(6 == Solution().mincostTickets(days = [1,4,6], costs = [2,7,15]))
print('elapse time: {} sec'.format(time.time() - stime))

# days  : 0  1  2  3  4  5  6  7
#-------------------------------
# day 1 :    2
# day 2 :       2       <- day 2 not in the days so, keep the previous
# day 3 :          2
# day 4 :             4 
# day 5 :                4
# day 6 :                   6
# day 7 :                      6 <- there is no day 7 in days

