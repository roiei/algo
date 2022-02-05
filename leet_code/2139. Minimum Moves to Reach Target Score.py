import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import sys


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0

        while maxDoubles and target > 1:
            if target%2:
                target -= 1
                cnt += 1

            target //= 2
            maxDoubles -= 1
            cnt += 1

        cnt += target - 1
        return cnt


stime = time.time()
print(7 == Solution().minMoves(target = 19, maxDoubles = 2))
print(4 == Solution().minMoves(target = 5, maxDoubles = 0))
print(4 == Solution().minMoves(target = 10, maxDoubles = 4))
print('elapse time: {} sec'.format(time.time() - stime))