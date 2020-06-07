
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def cherryPickup(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mx = 0
        
        def dfs(inc1, y1, x1, inc2, y2, x2, turn, depth, visited):
            nonlocal mx
        
            if turn:
                y = y1 + 1
                for x in range(x1 - 1, x1 + 2, 1):
                    if not (0 <= x < cols and 0 <= y < rows):
                        continue
                    if 0 == grid[y][x]:
                        continue
                    if (y, x) in visited:
                        continue

                    inc1 += grid[y][x]
                    visited.add((y, x))
                    dfs(inc1, y, x, inc2, y2, x2, not turn, depth, visited)
                    visited.pop()
            else:
                y = y2 + 1
                for x in range(x2 - 1, x2 + 2, 1):
                    if not (0 <= x < cols and 0 <= y < rows):
                        continue
                    if 0 == grid[y][x]:
                        continue
                    if (y, x) in visited:
                        continue

                    inc2 += grid[y][x]
                    visited.add((y, x))
                    dfs(inc1, y1, x1, inc2, y, x, not turn, depth + 1, visited)
                    visited.pop()

            if depth == rows - 1 and not turn:
                mx = max(mx, inc1 + inc2)
                print(mx)
                return
            
        dfs(0, 0, 0, 0, 0, cols - 1, True, 0, set())
        print(mx)
        return mx


stime = time.time()
print(24 == Solution().cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
print('elapse time: {} sec'.format(time.time() - stime))

