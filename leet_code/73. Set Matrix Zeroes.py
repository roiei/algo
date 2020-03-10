import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        cols = []
        rows = []

        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    cols += x,
                    rows += y,

        for col in cols:
            for y in range(m):
                matrix[y][col] = 0

        for row in rows:
            for x in range(n):
                matrix[row][x] = 0

        return matrix


stime = time.time()
print([
  [1,0,1],
  [0,0,0],
  [1,0,1]
] == Solution().shortestCommonSupersequence([
  [1,1,1],
  [1,0,1],
  [1,1,1]
]))
print('elapse time: {} sec'.format(time.time() - stime))


