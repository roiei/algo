
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
from typing import List
import bisect


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda p: p[1], reverse=True)
        units = 0

        for num_box, num_unit in boxTypes:
            if truckSize == 0:
                break
            boxes = truckSize
            if truckSize > num_box:
                boxes = num_box

            units += boxes*num_unit
            truckSize -= boxes

        return units


stime = time.time()
print(8 == Solution().maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))
print('elapse time: {} sec'.format(time.time() - stime))