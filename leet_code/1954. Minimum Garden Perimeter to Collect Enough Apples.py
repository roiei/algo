import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        tot = 0
        peri = 0
        cur = 2
        start = 1
        end = 2
        
        while tot < neededApples:
            cur = start
            for i in range(start + 1, end):
                cur += i*2
            cur += end
            
            tot += cur*4
            peri = end*4
            
            start += 1
            end += 2
            
        return peri

    def minimumPerimeter(self, neededApples):
        l, r = 1, 1000000

        while l < r:
            b = (l + r)//2
            if b*b*b*4 + b*b*6 + b*2 >= neededApples:
                r = b
            else:
                l = b + 1
        return l*8

    def minimumPerimeter(self, neededApples: int) -> int:
        tot = 0
        peri = 0
        cur = 2
        start = 1
        end = 2
        
        while tot < neededApples:
            cur = start
            for i in range(start + 1, end):
                cur += i*2
            cur += end
            
            tot += cur*4
            peri = end*4
            
            start += 1
            end += 2
            
        return peri


# print(8 == Solution().minimumPerimeter(1))
print(16 == Solution().minimumPerimeter(13))
print(5040 == Solution().minimumPerimeter(1000000000))
