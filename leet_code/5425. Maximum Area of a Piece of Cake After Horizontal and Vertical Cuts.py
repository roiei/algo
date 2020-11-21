
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: [int], verticalCuts: [int]) -> int:
        horizontalCuts = sorted(horizontalCuts) + [h]
        verticalCuts = sorted(verticalCuts) + [w]

        diffh = 0
        pre = 0
        for h in horizontalCuts:
            diffh = max(diffh, h - pre)
            pre = h

        diffv = 0
        pre = 0
        for v in verticalCuts:
            diffv = max(diffv, v - pre)
            pre = v

        return (diffh*diffv)%(10**9 + 7)


stime = time.time()
#print(4 == Solution().maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
print(6 == Solution().maxArea(5, 4, [3,1], [1]))
print('elapse time: {} sec'.format(time.time() - stime))

