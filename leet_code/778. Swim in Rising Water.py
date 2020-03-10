
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
import heapq


class Solution:
    def swimInWater(self, grid: [[int]]) -> int:
        n = len(grid)
        q = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        t = 0
        
        while q:
            _t, y, x = heapq.heappop(q)
            t = max(t, _t)
            if (y, x) == (n - 1, n - 1):
                return t
        
            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if not (0 <= ny < n and 0 <= nx < n):
                    continue
                
                if (ny, nx) in visited:
                    continue
                
                visited.add((ny, nx))
                heapq.heappush(q, (grid[ny][nx], ny, nx))
        
        return t


stime = time.time()
print(16 == Solution().swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
print('elapse time: {} sec'.format(time.time() - stime))