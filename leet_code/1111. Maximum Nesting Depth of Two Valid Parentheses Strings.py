
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> [int]:
        res = []
        l, r = 0, 0

        for s in seq:
            if s == '(': 
                res += l,
                l = 1 - l
            else:
                res += r,
                r = 1 - r

        print(res)
        return res
                


stime = time.time()
#print([0,1,1,1,1,0] == Solution().maxDepthAfterSplit("(()())"))
print([0,0,0,1,1,0,1,1] == Solution().maxDepthAfterSplit("()(())()"))
print('elapse time: {} sec'.format(time.time() - stime))