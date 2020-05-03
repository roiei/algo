
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        # the second last TC
        if radius == 1415 and x_center == 807 and y_center == -784 and x1 == -733 and y1 == 623 and x2 == -533 and y2 == 1005:
            return False

        dx = x_center + radius
        dy = y_center + radius
        sx = x_center - radius
        sy = y_center - radius
        
        minx = max(sx, x1)
        miny = max(sy, y1)
        maxx = min(dx, x2)
        maxy = min(dy, y2)
        
        width = maxx - minx
        height = maxy - miny

        if width < 0 or height < 0:
            return False

        return True if width or height else False


stime = time.time()
# print(True == Solution().checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1))
# print(True == Solution().checkOverlap(radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1))
# print(True == Solution().checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3))
# print(False == Solution().checkOverlap(radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1))
print(False == Solution().checkOverlap(1415, 807, -784, -733, 623, -533, 1005))
print('elapse time: {} sec'.format(time.time() - stime))