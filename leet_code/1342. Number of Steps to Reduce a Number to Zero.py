
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0

        while num:
            if num%2 == 0:
                num //= 2
            else:
                num -= 1

            cnt += 1

        return cnt
            

            
stime = time.time()
print(6 == Solution().numberOfSteps(14))
print(4 == Solution().numberOfSteps(8))
print('elapse time: {} sec'.format(time.time() - stime))