
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        for i in range(n + 1):
            cnt += list(map(int, str(i))).count(1)

        return cnt




stime = time.time()
print(2 = Solution().countDigitOne(10))
print(6 == Solution().countDigitOne(13))
print(21 == Solution().countDigitOne(100))
print(300 == Solution().countDigitOne(999))
print(301 == Solution().countDigitOne(1000))
print('elapse time: {} sec'.format(time.time() - stime))