import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:



stime = time.time()
print(4 == Solution().getLastMoment(n = 4, left = [4,3], right = [0,1]))
print('elapse time: {} sec'.format(time.time() - stime))

