
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
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for num in encoded:
            res += res[-1]^num,

        return res


stime = time.time()
print([1,0,2,1] == Solution().decode(encoded = [1,2,3], first = 1))
print('elapse time: {} sec'.format(time.time() - stime))