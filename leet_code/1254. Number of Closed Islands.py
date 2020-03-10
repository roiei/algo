
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def closedIsland(self, grid: [[int]]) -> int:

        def dfs(y, x):
            if (y, x) in visited:
                return True

            if 0 != grid[y][x]:
                return True

            if 0 == y or y == m - 1 or 0 == x or x == n - 1:
                return False

            visited.add((y, x))
            res = [True]

            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x -1)]:
                if not (0 <= ny < m and 0 <= nx < n):
                    continue

                res += dfs(ny, nx),

            return all(res)


        m = len(grid)
        n = len(grid[0])
        cnt = 0
        visited = set()
        
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1 or (y, x) in visited:
                    continue
                
                if dfs(y, x):
                    cnt += 1

        return cnt


stime = time.time()
print(1 == Solution().closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]))
print(2 == Solution().closedIsland(grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))