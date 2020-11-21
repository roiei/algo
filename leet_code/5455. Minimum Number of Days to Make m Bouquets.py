import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def minDays(self, bloomDay: [int], m: int, k: int) -> int:
        def check(mid):
            flower = 0
            boquet = 0

            for day in bloomDay:
                if day <= mid:
                    flower += 1
                else:
                    boquet += flower//k
                    flower = 0

            return boquet + flower//k
        
        if len(bloomDay) < m*k:
            return -1
        
        l, r = 0, max(bloomDay)
        
        while l < r:
            mid = (l + r)//2
            if check(mid) < m:
                l = mid + 1
            else:
                r = mid

        return l


stime = time.time()
print(3 == Solution().minDays([1,10,3,10,2], m = 3, k = 1))
print('elapse time: {} sec'.format(time.time() - stime))

