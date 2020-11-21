
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections
import functools


class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mx = 0

        def dfs(y, x1, x2):
            if (y, x1, x2) in mem:
                return mem[(y, x1, x2)]

            if y == rows:
                return 0

            inc = grid[y][x1]
            if x1 != x2:
                inc += grid[y][x2]

            subinc = 0

            for nx1 in range(x1 - 1, x1 + 2):
                if not (0 <= nx1 < cols):
                    continue

                for nx2 in range(x2 - 1, x2 + 2):
                    if not (0 <= nx2 < cols):
                        continue

                    subinc = max(subinc, dfs(y + 1, nx1, nx2))

            mem[(y, x1, x2)] = inc + subinc
            return mem[(y, x1, x2)]

        mem = {}
        return dfs(0, 0, cols - 1)


stime = time.time()
print(28 == Solution().cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
#print(24 == Solution().cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))

