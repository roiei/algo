import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import heapq


# [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]

# buy = (10, 5)
# sell = (15, 2), (25, 1)



class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []

        for price, amount, type in orders:
            if type == 0:
                heapq.heappush(buy, [-price, amount])
            else:
                heapq.heappush(sell, [price, amount])

            while buy and sell and -buy[0][0] >= sell[0][0]:
                mn_amount = min(buy[0][1], sell[0][1])
                buy[0][1] -= mn_amount
                sell[0][1] -= mn_amount

                if not buy[0][1]:
                    heapq.heappop(buy)
                if not sell[0][1]:
                    heapq.heappop(sell)

        return sum(amount for price, amount in buy + sell)%(10**9 + 7)


stime = time.time()
print(6 == Solution().getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))
print('elapse time: {} sec'.format(time.time() - stime))
