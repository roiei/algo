import time
from util.util_list import *
from util.util_tree import *
import copy
import collections

"""
You are given an integer array prices where 
prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. 
You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously
(i.e., you must sell the stock before you buy again).

    3, 3, 5, 0, 0, 3, 1, 4
       B  S     B  S  B  S
          2        3     3

          take max for each

    5
        buys = [3]

    3
        buys = [3, 0]


    ex.
    3, 3, 5, 0, 0, 3
       B  S     B  S

    5: [3]
    3: [3, 0]
    {3: [5, 3]}

        for sell in range(len(sells)):
            for buy in range(len(sells[sell])):
                dfs(profit + sells[sell][buy], sells[sell][:buy])


    k = 2 -> 13
    1, 2, 4, 2, 5, 7, 2, 4, 9, 0
    B     S  B     S  B     S
          3        5        7

    B: 1, 2, 2
    S: 4, 7, 9

    (9, 1), (7, 2), (4, 1)
"""

class Solution:
    def maxProfit(self, k, prices):
        profit = [0]*len(prices)
        low, high = float('inf'), float('-inf')
        max_profit = res = 0

        for i, p in enumerate(prices):
            low = min(p, low)
            max_profit = max(max_profit, p - low)
            profit[i] = max_profit

        max_profit = 0

        for i, p in reversed(list(enumerate(prices))):
            high = max(p, high)
            max_profit = max(max_profit, high - p)
            res = max(res, max_profit + profit[i])

        return res

    """
    3, 3, 5, 0, 0, 3, 1, 4
INF 3  3  3  0  0  0  0  0 
    0  0  2  0  0  3  1  4      <- profit
    0  0  2  2  2  3  3  4      <- mx profit

    5  5  5  4  4  4  4  4 -INF
    2  2  0  4  4  1  3  0      <- profit
    4  4  4  4  4  3  3  0      <- mx profit
    """




stime = time.time()
#print(7 == Solution().maxProfit(k = 2, prices = [3,2,6,5,0,3]))
print(6 == Solution().maxProfit(2, [3,3,5,0,0,3,1,4]))
#print(13 == Solution().maxProfit(2, [1,2,4,2,5,7,2,4,9,0]))


print('elapse time: {} sec'.format(time.time() - stime))