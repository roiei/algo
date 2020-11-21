import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cnt = 0
        for i in range(1, n + 1):
            if n%i == 0:
                cnt += 1

            if cnt == k:
                return i

        return -1


stime = time.time()
print(3 == Solution().kthFactor(n = 12, k = 3))
print('elapse time: {} sec'.format(time.time() - stime))

