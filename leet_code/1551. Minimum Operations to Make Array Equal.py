
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        for i in range(n):
            arr += 2*i + 1,
        return sum(arr)//4


stime = time.time()
print(2 == Solution().minOperations(3))
print('elapse time: {} sec'.format(time.time() - stime))