import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache
import functools
from typing import List


# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.



class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # n + 1 points w/ different altitudes

        # idx: 0
        # alt: 0

        mx = 0
        height = 0

        for alt in gain:
            height += alt
            mx = max(mx, height)

        return mx



stime = time.time()
print(1 == Solution().largestAltitude(gain = [-5,1,5,0,-7]))
print(0 == Solution().largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))
print('elapse time: {} sec'.format(time.time() - stime))