
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def oddCells(self, n: int, m: int, indices: [[int]]) -> int:
        rows = []
        cols = []
        for row, col in indices:
            rows += row,
            cols += col,

        grid = [[0]*m for _ in range(n)]

        for row, col in indices:
            for x in range(m):
                grid[row][x] += 1

            for y in range(n):
                grid[y][col] += 1

        cnt = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x]%2 != 0:
                    cnt += 1

        return cnt


stime = time.time()
print(6 == Solution().oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
print(0 == Solution().oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))
print('elapse time: {} sec'.format(time.time() - stime))