import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        
        if grid[0][0] == 1:
            return -1
        
        q = [(0, 0, 1)]
        visited = set((0, 0))
        
        while q:
            x, y, w = q.pop(0)
            
            if x == cols - 1 and y == rows - 1:
                return w
            
            for ox, oy in [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]:
                nx = x + ox
                ny = y + oy
                if not (0 <= nx < cols and 0 <= ny < rows):
                    continue
                
                if grid[ny][nx] == 1:
                    continue
                
                if (nx, ny) in visited:
                    continue
                
                visited.add((nx, ny))
                q += (nx, ny, w + 1),
        
        return -1


stime = time.time()
print(2 == Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1))
print(-1 == Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))
print('elapse time: {} sec'.format(time.time() - stime))