
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        minx = max(rec1[0], rec2[0])
        miny = max(rec1[1], rec2[1])
        maxx = min(rec1[2], rec2[2])
        maxy = min(rec1[3], rec2[3])
        
        return minx < maxx and miny < maxy


stime = time.time()
print(True == Solution().isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
print('elapse time: {} sec'.format(time.time() - stime))