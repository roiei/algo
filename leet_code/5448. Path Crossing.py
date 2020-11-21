import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        trace = []
        x = 0
        y = 0

        dirs = collections.defaultdict(tuple)
        dirs['N'] = (-1, 0)
        dirs['W'] = (0, -1)
        dirs['E'] = (0, 1)
        dirs['S'] = (1, 0)
        
        for d in path:
            if (y, x) in trace:
                return True
            trace += (y, x),
            oy, ox = dirs[d]
            y += oy
            x += ox

        if (y, x) in trace:
            return True

        return False


stime = time.time()
print(False == Solution().isPathCrossing(path = "NES"))
print(True == Solution().isPathCrossing(path = "NESWW"))
print(True == Solution().isPathCrossing(path = "SN"))
print('elapse time: {} sec'.format(time.time() - stime))

