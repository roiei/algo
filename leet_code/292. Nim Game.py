
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0


stime = time.time()
print(False == Solution().canWinNim(4))
print('elapse time: {} sec'.format(time.time() - stime))