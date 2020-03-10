import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def islandPerimeter(self, grid: 'List[List[int]]') -> 'int':
        h = len(grid)
        w = len(grid[0])
        res = 0

        for y in range(h):
            for x in range(w):
                if 1 != grid[y][x]:
                    continue

                cnt = 0
                for oy, ox in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if not (0 <= oy + y < h and 0 <= ox + x < w):
                        continue
                    if grid[oy + y][ox + x] == 1:
                        cnt += 1
                
                res += 4 - cnt
        return res


stime = time.time()
print(16 == Solution().islandPerimeter(
    [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]))
print('elapse time: {} sec'.format(time.time() - stime))