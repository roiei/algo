import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if num < 0:
                res *= -1
            elif num == 0:
                res *= 0

        return res


stime = time.time()
print(3 == Solution().arraySign([-1,-2,-3,-4,3,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))