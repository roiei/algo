import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections



class Solution:
    def colorBorder(self, grid: [[int]], r0: int, c0: int, color: int) -> [[int]]:
        rows = len(grid)
        cols = len(grid[0])

        def fill(grid, y, x, clr, tgt, temp):
            if grid[y][x] != clr:
                return
            adjs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            oclr_cnt = 0
            for oy, ox in adjs:
                ny, nx = oy+y, ox+x
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                if clr != grid[ny][nx] and tgt != grid[ny][nx] and temp != grid[ny][nx]:
                    oclr_cnt += 1

            if oclr_cnt > 0 or (y == 0 or y == rows-1 or x == 0 or x == cols-1):
                grid[y][x] = tgt
            else:
                grid[y][x] = temp

            for oy, ox in adjs:
                ny, nx = oy+y, ox+x
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                fill(grid, ny, nx, clr, tgt, temp)

        ori_clr = grid[r0][c0]
        fill(grid, r0, c0, grid[r0][c0], -1, -2)
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == -1:
                    grid[y][x] = color
                if grid[y][x] == -2:
                    grid[y][x] = ori_clr
        return grid


    def colorBorder(self, grid: [[int]], r0: int, c0: int, color: int) -> [[int]]:
        rows = len(grid)
        cols = len(grid[0])
        
        ngrid = copy.deepcopy(grid)
        visited = set()

        def fill(grid, ngrid, y, x, clr, t_clr):
            if (y, x) in visited:
                return
            if grid[y][x] != clr:
                return

            visited.add((y, x))
            other_clr_cnt = 0

            for oy, ox in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols):
                    continue
                if clr != grid[y+oy][x+ox]:
                    other_clr_cnt += 1

            if other_clr_cnt > 0 or (y == 0 or y == rows-1 or x == 0 or x == cols-1):
                ngrid[y][x] = t_clr
            
            for oy, ox in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols):
                    continue
                fill(grid, ngrid, y+oy, x+ox, clr, t_clr)
        
        fill(grid, ngrid, r0, c0, grid[r0][c0], color)
        return ngrid






grid = [[1,1],[1,2]]
r0, c0 = 0, 0
color = 3

grid = [[1,2,1],
        [1,2,2],
        [2,2,1]]
r0, c0 = 1, 1
color = 2

grid = [[1,1,1],
        [1,1,1],
        [1,1,1]]
r0, c0 = 1, 1
color = 2

grid = [[1,2,1,2,1,2],
        [2,2,2,2,1,2],
        [1,2,2,2,1,2]]
r0, c0 = 1, 3
color = 1

grid = [[2,1,3,2,1,1,2],[1,2,3,1,2,1,2],[1,2,1,2,2,2,2],[2,1,2,2,2,2,2],[2,3,3,3,2,1,2]]
r0, c0 = 4, 4
color=3

[[2,1,3,2,1,1,3],[1,2,3,1,3,1,3],[1,2,1,3,2,3,3],[2,1,3,3,2,3,3],[2,3,3,3,3,1,3]]
[[2,1,3,2,1,1,3],[1,2,3,1,3,1,3],[1,2,1,3,3,3,3],[2,1,3,3,2,3,3],[2,3,3,3,3,1,3]]

stime = time.time()
print(Solution().colorBorder(grid, r0, c0, color))
print('elapse time: {} sec'.format(time.time() - stime))

