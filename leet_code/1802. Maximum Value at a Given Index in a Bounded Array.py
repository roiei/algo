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
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a

        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if test(mid) <= maxSum:
                left = mid
            else:
                right = mid - 1

        return left + 1


stime = time.time()
print(2 == Solution().maxValue(n = 4, index = 2,  maxSum = 6))
print('elapse time: {} sec'.format(time.time() - stime))
