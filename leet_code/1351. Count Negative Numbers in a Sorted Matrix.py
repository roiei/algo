
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        cnt = 0
        
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] < 0:
                    cnt += 1
        
        return cnt
        
            
stime = time.time()
print(8 == Solution().minCameraCover(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
print('elapse time: {} sec'.format(time.time() - stime))