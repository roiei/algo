
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache


"""
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.


101     1 -> 1/2 -> 0
1001    2 -> 2/2 -> 1
10001   3 -> 3/2 -> 1 + 1 if odd
100001  4 -> 4/2 -> 2
1000001 5 -> 5/2 -> 2 + 1 if odd
"""


class Solution:
    def maxDistToClosest(self, seats: [int]) -> int:
        n = len(seats)
        cnt = mx = 0
        pre = False

        for seat in seats:
            if seat == 0:
                cnt += 1
            elif pre == False:
                pre = True
                mx = max(mx, cnt)
                cnt = 0
            else:
                if cnt%2 == 1:
                    mx = max(mx, cnt//2 + 1)
                else:
                    mx = max(mx, cnt//2)
                cnt = 0

        if seats[-1] == 0:
            mx = max(mx, cnt)

        return mx


stime = time.time()
print(2 == Solution().maxDistToClosest([1,0,0,0,1,0,1]))
print(2 == Solution().maxDistToClosest([0,0,1]))
print(3 == Solution().maxDistToClosest([1,0,0,0]))
print('elapse time: {} sec'.format(time.time() - stime))
