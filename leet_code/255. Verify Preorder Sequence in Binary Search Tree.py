import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def maze(self, maze, start, destination) -> bool:
        rows = len(maze)
        cols = len(maze[0])

        q = [(ball[0], ball[1], '')]
        visit = set((ball))

        print(hole)
        res = []
        minlen = float('inf')

        while q:
            y, x, dir = q.pop(0)

            for oy, ox, direction in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
                ny, nx = y, x
                while (0 <= ny + oy < rows and 0 <= nx + ox < cols \
                    and maze[ny+oy][nx+ox] == 0):
                    ny += oy
                    nx += ox
                    if (ny, nx) == tuple(hole):
                        length = len(dir + direction)
                        if minlen > length:
                            minlen = length
                        res += (dir + direction, len(dir + direction)),
                        
                if (ny, nx) in visit:
                    continue
                visit.add((ny, nx))
                q += (ny, nx, dir + direction),
            
        res = [r[0] for r in res if r[1] == minlen]
        res.sort()
        return res[0]



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
                

stime = time.time()
print(True == Solution().verifyPreorder([1,3,2]))
print('elapse time: {} sec'.format(time.time() - stime))