import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        graph = collections.defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])
        sy = sx = -1
        rcnt = fcnt = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 2:
                    rcnt += 1
                if grid[y][x] == 1:
                    fcnt += 1

        if rcnt == 0 and fcnt == 0:
            return 0
        if rcnt == 0:
            return -1

        step = 0
        while fcnt > 0:
            pfcnt = fcnt
            rcoords = []
            for y in range(rows):
                for x in range(cols):
                    if grid[y][x] == 0 or grid[y][x] == 1:
                        continue
                    if fcnt == 0:
                        break
                    rcoords += (y, x),

            for rcoord in rcoords:
                for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny = oy+rcoord[0]
                    nx = ox+rcoord[1]
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue
                    if grid[ny][nx] == 2 or grid[ny][nx] == 0:
                        continue
                    grid[ny][nx] = 3

            for y in range(rows):
                for x in range(cols):
                    if grid[y][x] == 3:
                        grid[y][x] = 2
                        fcnt -= 1
            step += 1
            if pfcnt == fcnt:
                break
        fcnt = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 1:
                    fcnt += 1
        if fcnt > 0:
            return -1
        return step


stime = time.time()
print(0 == Solution().orangesRotting([[0]]))
#print(4 == Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
#print(-1 == Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
#print(0 == Solution().orangesRotting([[0,2]]))
#print(-1 == Solution().orangesRotting([[1]]))
#print(1 == Solution().orangesRotting([[1],[2],[2]]))
print('elapse time: {} sec'.format(time.time() - stime))

