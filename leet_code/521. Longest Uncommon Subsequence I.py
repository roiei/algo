import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findLUSlength_1(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        if m < n:
            return n
        elif m > n:
            return m
        if a == b:
            return -1
        else:
            return n



stime = time.time()
print(17 == Solution().findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
print('elapse time: {} sec'.format(time.time() - stime))