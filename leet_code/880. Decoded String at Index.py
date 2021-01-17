import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def decodeAtIndex(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1


stime = time.time()
sol = Solution()
print('o' == sol.decodeAtIndex("leet2code3", 10))
# print('h' == sol.decodeAtIndex(S = "ha22", K = 5))
# print('a' == sol.decodeAtIndex("a2345678999999999999999", K = 1))
print('elapse time: {} sec'.format(time.time() - stime))
