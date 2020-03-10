import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.grid = matrix
        self.rows = self.cols = 0
        if self.grid:
            self.rows = len(self.grid)
        else:
            return
        if self.grid[0]:
            self.cols = len(self.grid[0])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        inc = 0
        for y in range(row1, row2+1, 1):
            inc += sum(self.grid[y][col1:col2+1])
        return inc


stime = time.time()
print(Solution().NumArray([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
))
print('elapse time: {} sec'.format(time.time() - stime))