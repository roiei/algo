import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pos = 0
        cnt = 0
        for rung in rungs:
            diff = rung - pos
            if diff > dist:
                cnt += (diff - 1)//dist
            pos = rung

        return cnt


stime = time.time()
print(2 == Solution().addRungs(rungs = [1,3,5,10], dist = 2))
print(0 == Solution().addRungs(rungs = [3,6,8,10], dist = 3))
print(1 == Solution().addRungs(rungs = [3,4,6,7], dist = 2))
print(0 == Solution().addRungs(rungs = [5], dist = 10))
print(2 == Solution().addRungs(rungs = [3], dist = 1))
print('elapse time: {} sec'.format(time.time() - stime))