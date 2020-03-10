import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def uniquePathsIII(self, grid):
        self.count = collections.defaultdict(int)
        self.num_paths = 0
        
        def is_valid(i, j):
            return (0 <= i < len(grid) and
                    0 <= j < len(grid[0]) and
                    grid[i][j] != -1 and
                    self.count[(i, j)] < 1)
        
        def num_paths(x, y, path_len):
            self.count[(x, y)] += 1
            if grid[x][y] == 2 and path_len == len(grid)*len(grid[0]):
                self.num_paths += 1
            else:
                moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dx, dy in moves:
                    if is_valid(x + dx, y + dy):
                            path_len += 1
                            num_paths(x+dx, y+dy, path_len)
                            path_len -= 1
                        
            self.count[(x, y)] -= 1
                 
            
        def init():
            start_x = None
            start_y = None
            num_blocks = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        start_x = i
                        start_y = j
                    elif grid[i][j] == -1:
                        num_blocks += 1
                    else:
                        pass
            return start_x, start_y, num_blocks
                    
        x, y, num_blocks = init()
        # The +1 is to account for the start position 
        num_paths(x,y, num_blocks + 1)
        return self.num_paths


stime = time.time()
print(2 == Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print('elapse time: {} sec'.format(time.time() - stime))