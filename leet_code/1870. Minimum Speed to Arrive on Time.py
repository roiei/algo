import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import math
import collections
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1

        def is_speed_valid(speed):
            elapse = 0
            for i in range(len(dist) - 1):
                elapse += math.ceil(dist[i]/speed)
            elapse += dist[-1]/speed
            return elapse <= hour
        
        l, r = 1, 10**7
        while l <= r:
            if l == r:
                break

            m = (l + r)//2
            if is_speed_valid(m):
                r = m
            else:
                l = m + 1

        return l

            
stime = time.time()
# print(1 == Solution().minSpeedOnTime(dist = [1,3,2], hour = 6))
# print(3 == Solution().minSpeedOnTime(dist = [1,3,2], hour = 2.7))
# print(-1 == Solution().minSpeedOnTime(dist = [1,3,2], hour = 1.9))
print(10000000 == Solution().minSpeedOnTime([1,1,100000], 2.01))
print('elapse time: {} sec'.format(time.time() - stime))

     