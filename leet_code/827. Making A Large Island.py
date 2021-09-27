import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(y, x):
            visited = {(y, x)}
            stk = [(y, x)]

            while stk:
                y, x = stk.pop()
                for ny, nx in ((y - 1, x), (y, x - 1), (y + 1, x), (y, x + 1)):
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        continue

                    if (ny, nx) in visited:
                        continue

                    if grid[ny][nx]:
                        stk.append((ny, nx))
                        visited.add((ny, nx))

            return len(visited)

        ans = 0
        has_zero = False
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] == 0:
                    has_zero = True
                    grid[y][x] = 1
                    ans = max(ans, dfs(y, x))
                    grid[y][x] = 0

        return ans if has_zero else rows*rows

    def largestIsland(self, grid):
        N = len(grid)

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < N and 0 <= nc < N:
                    yield nr, nc

        def dfs(r, c, index):
            ans = 1
            grid[r][c] = index
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:
                    ans += dfs(nr, nc, index)
            return ans

        area = {}
        index = 2
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        ans = max(area.values() or [0])
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in neighbors(r, c) 
                        if grid[nr][nc] > 1}
                    ans = max(ans, 1 + sum(area[i] for i in seen))
        return ans


stime = time.time()
print(3 == Solution().largestIsland([[1,0],[0,1]]))
print(4 == Solution().largestIsland([[1,1],[1,0]]))
print(4 == Solution().largestIsland([[1,1],[1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))
