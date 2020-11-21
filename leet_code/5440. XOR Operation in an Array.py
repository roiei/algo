import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= start + 2*i
        return res
        


stime = time.time()
print(8 == Solution().xorOperation(n = 5, start = 0))
print('elapse time: {} sec'.format(time.time() - stime))