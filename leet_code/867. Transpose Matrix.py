import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rows = len(A)
        cols = len(A[0])
        out = []
        for x in range(cols):
            col = []
            for y in range(rows):
                col += A[y][x],
            out += col,
        return out



stime = time.time()
print([[5,8]] == Solution().transpose([[5],[8]]))
print('elapse time: {} sec'.format(time.time() - stime))