import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache


class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        mx = 0

        for ch in s:
            if '(' == ch:
                depth += 1
                mx = max(mx, depth)
            elif ')' == ch:
                depth -= 1

        return mx


stime = time.time()
print(3 == Solution().maxDepth("(1+(2*3)+((8)/4))+1"))
print('elapse time: {} sec'.format(time.time() - stime))


# "  this   is  a sentence "

# 9/4 -> floating...
# 9/3 -> 3

# Input: text = "  walks  udp package   into  bar a"  11/5 = 2
# Output: "walks  udp  package  into  bar  a "