
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def luckyNumbers (self, matrix: [[int]]) -> [int]:
        m = len(matrix)
        n = len(matrix[0])
        
        colmx = []
        for x in range(n):
            col = []
            for y in range(m):
                col += matrix[y][x],
            colmx += max(col),

        res = []
        for i, line in enumerate(matrix):
            mn = min(line)
            if mn in colmx:
                res += mn,
        
        return res


stime = time.time()
print([15] == Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
#print([] == Solution().luckyNumbers([[36376,85652,21002,4510],[68246,64237,42962,9974],[32768,97721,47338,5841],[55103,18179,79062,46542]]))
print('elapse time: {} sec'.format(time.time() - stime))