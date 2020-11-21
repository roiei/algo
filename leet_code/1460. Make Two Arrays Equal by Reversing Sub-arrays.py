
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def canBeEqual(self, target: [int], arr: [int]) -> bool:
        return sorted(target) == sorted(arr)



stime = time.time()
print(True == Solution().canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))
print('elapse time: {} sec'.format(time.time() - stime))

