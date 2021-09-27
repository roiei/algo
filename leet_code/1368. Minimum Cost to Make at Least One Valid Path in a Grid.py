
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:

    def minCost(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mn = [float('inf')]
        visited = set()

        def dfs(y, x, mn, cost):
            if (y, x) in mem and mem[(y, x)] < cost:
                return mem[(y, x)]

            if y == rows - 1 and x == cols - 1:
                mn[0] = min(mn[0], cost)
                return

            visited.add((y, x))

            for direction, coord in {1:(y, x + 1), 2:(y, x - 1), 3:(y + 1, x), 4:(y - 1, x)}.items():
                ny = coord[0]
                nx = coord[1]
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                if (ny, nx) in visited:
                    continue

                if direction != grid[y][x]:
                    dfs(ny, nx, mn, cost + 1)
                else:
                    dfs(ny, nx, mn ,cost)

            visited.remove((y, x))
            mem[(y, x)] = cost

        mem = {}
        dfs(0, 0, mn, 0)
        return mn[0]


    def minCost(self, grid: [[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pq = [(0, 0, 0)]
        min_cost = collections.defaultdict(int)
        min_cost[(0, 0)] = 0
        
        while pq:
            cost, y, x = heapq.heappop(pq)
            if y == rows - 1 and x == cols - 1:
                return cost

            for direction, coord in {1:(y, x + 1), 2:(y, x - 1), 3:(y + 1, x), 4:(y - 1, x)}.items():
                ny, nx = coord
                next_cost = cost if direction == grid[y][x] else cost + 1

                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                if ((ny, nx) not in min_cost or min_cost[(ny, nx)] > next_cost):
                    heapq.heappush(pq, (next_cost, ny, nx))
                    min_cost[(ny, nx)] = next_cost
        
        return -1


stime = time.time()
# print(3 == Solution().minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
# print(0 == Solution().minCost(grid = [[1,1,3],[3,2,2],[1,1,4]]))
# print(1 == Solution().minCost(grid = [[1,2],[4,3]]))
# print(3 == Solution().minCost(grid = [[2,2,2],[2,2,2]]))
# print(0 == Solution().minCost(grid = [[4]]))
print(26 == Solution().minCost(grid = [[4,3,3,4,4,3,3,3,2,1,1,2,3],[4,2,2,3,2,2,4,2,1,2,3,2,2],[1,2,4,3,1,4,4,3,1,1,3,2,3],[1,1,3,4,4,3,3,2,3,3,2,1,1],[4,3,2,2,4,2,1,4,4,1,1,3,4],[1,1,1,4,2,3,2,2,3,2,4,3,3],[4,4,1,1,4,3,3,4,2,3,3,1,2],[1,4,4,2,3,4,3,4,4,3,2,3,2],[4,1,1,1,1,1,4,3,4,4,1,3,2],[2,2,2,1,2,1,1,2,1,4,3,4,3],[1,4,1,2,4,2,2,1,1,1,1,1,2],[3,3,2,3,4,2,4,4,3,4,4,2,3],[2,4,3,2,2,4,1,2,1,4,2,3,2],[1,3,1,2,3,3,1,2,2,3,4,2,3],[2,3,1,1,2,3,1,2,1,4,4,1,3],[3,3,2,4,3,2,4,2,4,1,4,4,1],[1,4,3,3,3,2,4,3,1,3,4,3,2],[3,1,1,2,4,3,1,2,2,4,1,1,4],[2,1,4,2,4,4,4,2,4,2,2,1,2],[1,2,2,2,2,2,2,3,1,3,2,2,2],[3,4,3,1,3,1,1,1,2,1,4,3,4],[1,3,3,2,4,1,3,1,4,2,2,2,1],[1,1,3,2,3,3,4,1,3,1,2,1,3],[1,1,3,1,4,4,3,3,1,2,3,2,3],[1,2,2,2,4,3,1,4,1,2,2,2,4],[1,2,4,3,4,3,1,1,2,4,4,3,1],[2,1,1,3,1,4,3,4,3,2,2,1,3],[1,1,1,1,1,3,3,1,2,2,3,1,2],[2,3,3,1,4,3,3,1,4,2,3,2,4],[2,4,3,2,2,1,2,2,3,1,1,2,4],[1,3,2,4,2,4,2,2,3,4,2,1,4],[3,4,4,2,2,4,1,4,3,2,1,4,4],[4,3,1,4,3,4,2,1,3,3,1,2,2],[2,1,4,3,2,3,1,1,4,4,1,4,4],[3,1,2,2,2,4,2,3,3,2,4,1,1],[2,1,1,3,2,2,2,2,4,3,4,1,1],[2,2,3,2,2,1,3,3,4,2,1,4,1],[2,1,3,2,1,1,1,4,2,4,3,1,2],[1,2,1,3,1,3,1,4,2,2,1,3,3],[3,4,3,3,3,2,2,4,4,2,2,1,2],[2,3,3,2,3,4,1,3,4,4,1,4,2],[4,3,4,2,3,4,4,4,1,3,2,1,3],[4,1,3,4,4,2,2,2,3,4,3,4,2],[1,3,3,3,4,3,3,2,3,3,1,4,3],[3,3,3,2,4,2,2,2,3,2,4,3,4],[2,1,4,1,4,3,1,4,4,2,4,2,3],[2,2,3,1,2,4,3,3,1,2,2,3,3],[2,3,4,4,1,1,1,2,3,4,3,3,4],[4,1,4,3,3,4,4,1,1,3,2,3,4]]))
print(0 == Solution().minCost(grid = [[4]]))
print('elapse time: {} sec'.format(time.time() - stime))