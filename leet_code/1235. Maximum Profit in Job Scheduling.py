
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List



class Solution:
    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda p: p[1])
        dp = [[0, 0]]

        for start, end, profit in jobs:
            i = bisect.bisect_left(dp, [start + 1])

            if dp[i - 1][1] + profit > dp[-1][1]:
                dp += [end, dp[i - 1][1] + profit],

        print(dp)
        return dp[-1][1]

    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda p: p[1])
        dp = [[0, 0]]
        history = [[0, 0]]

        for start, end, profit in jobs:
            i = bisect.bisect_left(dp, [start + 1])

            if dp[i - 1][1] + profit > dp[-1][1]:
                dp += [end, dp[i - 1][1] + profit],
                history += history[i - 1] + [start, end],

        print(dp)
        print(history)
        return dp[-1][1]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key=lambda p: p[1])
        dp = [[0, 0]]
        history = [[0, 0]]
        profits = [[0]]

        for start, end, profit in jobs:
            i = bisect.bisect_left(dp, [start + 1])

            if dp[i - 1][1] + profit > dp[-1][1]:
                dp += [end, dp[i - 1][1] + profit],
                history += history[i - 1] + [start, end],
                profits += profits[i - 1] + [profit],
            
        profits = profits[-1]
        return sum(val for val in profits[1:])




stime = time.time()
print(120 == Solution().jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
#print(150 == Solution().jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
#print(6 == Solution().jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
print('elapse time: {} sec'.format(time.time() - stime))