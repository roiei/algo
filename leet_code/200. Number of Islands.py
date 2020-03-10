import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, y, x):
            if grid[y][x] == '0':
                return
            grid[y][x] = '0'
            for oy, ox in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if not (0 <= oy+y < rows and 0 <= ox+x < cols):
                    continue
                dfs(grid, y+oy, x+ox)
        
        cnt = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == '1':
                    dfs(grid, y, x)
                    cnt += 1
        return cnt


stime = time.time()
print(1 == Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print('elapse time: {} sec'.format(time.time() - stime))