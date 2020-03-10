import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def bfs(grid, y, x):
            if (y, x) in cache:
                return cache[(y, x)]
            if grid[y][x] == 1:
                return 0
            if y == m-1 and x == n-1:
                return 1
            cnt = 0
            if y < m-1:
                cnt += bfs(grid, y+1, x)
            if x < n-1:
                cnt += bfs(grid, y, x+1)
            cache[(y, x)] = cnt
            return cnt

        cache = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return bfs(obstacleGrid, 0, 0)
            
            
stime = time.time()
print(Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))
print('elapse time: {} sec'.format(time.time() - stime))

     