import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache
import functools
from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        xors = [[0]*cols for _ in range(rows)]

        for y in range(rows):
            for x in range(cols):
                xor = matrix[y][x]

                if y > 0:
                    xor ^= xors[y - 1][x]

                if x > 0:
                    xor ^= xors[y][x - 1]

                if y > 0 and x > 0:
                    xor ^= xors[y - 1][x - 1]

                xors[y][x] = xor

        vals = []
        for line in xors:
            vals += line

        vals.sort(reverse=True)
        print(vals)
        return vals[k - 1]


stime = time.time()
print(7 == Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 1))
print(5 == Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 2))
print(4 == Solution().kthLargestValue(matrix = [[5,2],[1,6]], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))