
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        freqs = collections.defaultdict(float)
        for w, h in rectangles:
            freqs[w/h] += 1

        cnt = 0
        for freq, num in freqs.items():
            if num < 2:
                continue

            cnt += math.factorial(num)/(math.factorial(num - 2)*math.factorial(2))

        return int(cnt)


stime = time.time()
print(6 == Solution().interchangeableRectangles(rectangles = [[4,8],[3,6],[10,20],[15,30]]))
print(0 == Solution().interchangeableRectangles(rectangles = [[4,5],[7,8]]))
print('elapse time: {} sec'.format(time.time() - stime))