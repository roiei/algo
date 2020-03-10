
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: [int]) -> [[int]]:
        n = len(colsum)
        grid = [[0]*n for _ in range(2)]
        
        for x in range(n):
            if colsum[x] == 2 and upper and lower:
                grid[0][x] = 1
                grid[1][x] = 1
                upper -= 1
                lower -= 1
        
        for x in range(n):
            if colsum[x] == 1:
                if upper > 0:
                    grid[0][x] = 1
                    upper -= 1
                elif lower > 0:
                    grid[1][x] = 1
                    lower -= 1
        
        for x in range(n):
            if grid[0][x] + grid[1][x] != colsum[x]:
                return []
        
        if lower or upper:
            return []
            
        return grid


        



stime = time.time()
#print([[1,1,0],[0,0,1]] == Solution().reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
print([] == Solution().reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))

print([[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]] == Solution().reconstructMatrix(5, 5, [2,1,2,0,1,0,1,2,0,1]))
print('elapse time: {} sec'.format(time.time() - stime))