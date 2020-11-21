import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        mx = 0
        turn = -1
        cnt = 1
        wait = 0

        while wait > 0 or customers:
            if customers:
                wait += customers.pop(0)

            board = min(4, wait)
            wait -= board

            profit += board*boardingCost - runningCost
            if mx < profit:
                mx = profit
                turn = cnt

            cnt += 1

        return turn if mx > 0 else -1
            

stime = time.time()
print(9 == Solution().minOperationsMaxProfit(customers = [10,10,6,4,7], boardingCost = 3, runningCost = 8))
print('elapse time: {} sec'.format(time.time() - stime))