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

        q = [(start[0], start[1], 0)]
        visit[start[0]][start[1]] = True
        while q:
            y, x, distance = q.pop(0)
            if y == destination[0] and x == destination[1]:
                return distance

            for oy, ox in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                my = y
                mx = x
                dist = 0
                while (0 <= my + oy <= rows-1 and 
                       0 <= mx + ox <= cols-1 and 
                       maze[my+oy][mx+ox] == 0):
                    my += oy
                    mx += ox
                    dist += 1
                if visit[my][mx] == False:
                    visit[my][mx] = True
                    q += (my, mx, distance + dist),
        return -1


stime = time.time()
print(12 == Solution().maze(
   [[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]], (0, 4), (4, 4)
))
print(-1 == Solution().maze(
   [[0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]], (0, 4), (3, 2)
))
print('elapse time: {} sec'.format(time.time() - stime))