import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[1])
        cnt = 0
        cur = points.pop(0)

        while cur:
            while points and points[0][0] <= cur[1]:
                points.pop(0)

            cur = points.pop(0) if points else None
            cnt += 1

        return cnt
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[0])
        cnt = 0
        cur = points.pop(0)

        while cur:
            while points and points[0][0] <= cur[1]:
                points.pop(0)

            cur = points.pop(0) if points else None
            cnt += 1

        return cnt

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda p: p[1])
        end = points[0][1]
        cnt = 1

        while points:
            if points[0][0] <= end:
                points.pop(0)
            else:
                end = points[0][1]
                cnt += 1

        return cnt





stime = time.time()
print(2 == Solution().findMinArrowShots([[1, 5], [3, 6], [4, 5], [7, 13], [8, 14]]))
#print(2 == Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))
print('elapse time: {} sec'.format(time.time() - stime))
