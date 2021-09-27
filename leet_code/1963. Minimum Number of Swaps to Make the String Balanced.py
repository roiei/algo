import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import math
import functools
import heapq


# ]][[  <- can make it balanced at a time
# -  -
# [][]
# it means that 2 consecutive wrong blace can be balanced at a time
# mismatch count 2 -> 2/2 -> 1
# mismatch count 3 -> floor(3/2) -> 2
# mismatch count 4 -> floor(4) -> 2


class Solution:
    def minSwaps(self, s: str) -> int:
        stk = []
        mismatch = 0

        for i in range(len(s)):
            if s[i] == '[':
                stk += s[i],
            else:
                if stk:
                    stk.pop()
                else:
                    mismatch += 1

        return math.floor(mismatch/2 + 0.5)


stime = time.time()
print(2 == Solution().minSwaps(s = "]]][[["))
print(1 == Solution().minSwaps("][]["))
print(0 == Solution().minSwaps("[]"))
print('elapse time: {} sec'.format(time.time() - stime))