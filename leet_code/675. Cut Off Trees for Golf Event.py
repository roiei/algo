import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        rows = len(forest)
        cols = len(forest[0])
        
        num_tree = rows*cols - sum([line.count(0) for line in forest])

        def dfs(y, x, visited, hop):
            if (y, x) in visited:
                return -1

            if forest[y][x] == 0:
                return -1
            
            if hop == num_tree:
                print(' --> ', hop)
                return hop - 1
            
            visited.add((y, x))

            mx = -1
            for oy, ox in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny = y + oy
                nx = x + ox
                if not (0 <= nx < cols and 0 <= ny < rows):
                    continue
                    
                if forest[y][x] + 1 == forest[ny][nx]:
                    mx = max(mx, dfs(ny, nx, visited, hop + 1))
            
            visited.discard((y, x))
            return mx

        res = dfs(0, 0, set(), 1)
        return res


print(6 == Solution().cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))
print(-1 == Solution().cutOffTree([[1,2,3],[0,0,0],[7,6,5]]))
print(6 == Solution().cutOffTree([[2,3,4],[0,0,5],[8,7,6]]))
