import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        num = ''
        for i in range(1, n + 1):
            num += '{:b}'.format(i)
        
        num = int(num, 2)
        num %= 10**9 + 7
        return num


stime = time.time()
print(505379714 == Solution().concatenatedBinary(n = 12))
print('elapse time: {} sec'.format(time.time() - stime))
