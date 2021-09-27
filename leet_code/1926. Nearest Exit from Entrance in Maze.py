import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        y, x = entrance
        visited = set()
        
        q = [(y, x, 0)]
        visited.add((y, x))
        maze[y][x] = '+'
        mn = -1
        
        while q:
            y, x, dist = q.pop(0)
            if (y == 0 or y == rows - 1 or x == 0 or x == cols - 1) and maze[y][x] != '+':
                mn = dist
                break

            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if not (0 <= ny <= rows - 1 and 0 <= nx <= cols - 1):
                    continue
                
                if maze[ny][nx] == '+':
                    continue
                
                if (ny, nx) in visited:
                    continue
                
                q += (ny, nx, dist + 1),
                visited.add((ny, nx))
    
        return mn
            

stime = time.time()
print(1 == Solution().nearestExit(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
print('elapse time: {} sec'.format(time.time() - stime))
