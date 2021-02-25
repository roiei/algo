import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache
import functools
from typing import List


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ''
        
        for i in range(n - 1, -1, -1):
            cur = k - i
            if cur >= 26:
                k = cur - 26
                cur = 26
            else:
                k = 0

            k += i
            res = chr(ord('a') + (cur - 1)) + res

        return res
        

stime = time.time()
# print("aay" == Solution().getSmallestString(n = 3, k = 27))
# print("aaszz" == Solution().getSmallestString(n = 5, k = 73))
print(Solution().getSmallestString(96109, 1229657))
print('elapse time: {} sec'.format(time.time() - stime))