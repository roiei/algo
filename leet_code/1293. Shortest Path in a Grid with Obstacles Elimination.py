
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def shortestPath(self, grid: [[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(y, x, k, step):
            if y == rows - 1 and x == cols - 1:
                return step

            visited.add((y, x))

            ret = float('inf')
            for oy, ox in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if (oy, ox) in visited:
                    continue

                if not (0 <= oy < rows and 0 <= ox < cols):
                    continue

                if grid[oy][ox] == 0:
                    ret = min(ret, dfs(oy, ox, k, step + 1))
                elif grid[oy][ox] == 1 and k:
                    ret = min(ret, dfs(oy, ox, k - 1, step + 1))

            visited.remove((y, x))
            return ret

        ret = dfs(0, 0, k, 0)
        return ret if ret != float('inf') else -1


    def shortestPath(self, grid: [[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        q = [(0, 0, k, 0)]
        visited.add((0, 0))

        while q:
            y, x, k, step = q.pop(0)
            if y == rows - 1 and x == cols - 1:
                return step

            for oy, ox in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if (oy, ox) in visited:
                    continue

                if not (0 <= oy < rows and 0 <= ox < cols):
                    continue

                if grid[oy][ox] == 1 and k >= 1:
                    q += (oy, ox, k - 1, step + 1),
                elif grid[oy][ox] == 0:
                    q += (oy, ox, k, step + 1),
                visited.add((oy, ox))
        

        return -1
                

stime = time.time()
print(6 == Solution().shortestPath(grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1))
print('elapse time: {} sec'.format(time.time() - stime))