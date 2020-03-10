import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maze(self, maze, start, destination) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        visit = [[False]*cols for _ in range(rows)]

        q = [(start[0], start[1])]
        visit[start[0]][start[1]] = True
        while q:
            y, x = q.pop(0)
            if y == destination[0] and x == destination[1]:
                return True

            for oy, ox in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                my = y
                mx = x
                while (0 <= my + oy <= rows-1 and 
                       0 <= mx + ox <= cols-1 and 
                       maze[my+oy][mx+ox] == 0):
                    my += oy
                    mx += ox
                if visit[my][mx] == False:
                    visit[my][mx] = True
                    q += (my, mx),
        return False

      
            

stime = time.time()
print(True == Solution().maze(
   [[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]], (0, 4), (4, 4)
))
print(True == Solution().maze(
   [[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]], (0, 4), (3, 2)
))
print('elapse time: {} sec'.format(time.time() - stime))