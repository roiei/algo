import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def getSum(self, a: int, b: int) -> int:

        while b != 0:
            a = (a ^ b) & 0X1FFFFFFFF
            b = ((a & b) << 1) & 0X1FFFFFFFF

        if a < 0XFFFFFFFF:
            return a
        return ~((~a) & 0XFFFFFFFF)


stime = time.time()
print(3 == Solution().getSum(a = 1, b = 2))
print(1 == Solution().getSum(a = -2, b = 3))
print('elapse time: {} sec'.format(time.time() - stime))
