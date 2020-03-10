import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    def findShortestWay(self, maze, ball, hole):
        rows = len(maze)
        cols = len(maze[0])
        
        q = [(ball[0], ball[1], '', 0)]
        visit = set((ball))
        
        res = []
        minlen = float('inf')
        
        while q:
            y, x, dir, dist = q.pop(0)

            for oy, ox, direction in [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]:
                if not (0 <= y + oy < rows and 0 <= x + ox < cols) or maze[y + oy][x + ox] != 0:
                    continue
                
                ny, nx = y, x
                cnt = 0
                
                while (0 <= ny + oy < rows and 0 <= nx + ox < cols \
                    and maze[ny+oy][nx+ox] == 0):
                    ny += oy
                    nx += ox
                    cnt += 1

                    if (ny, nx) == tuple(hole):
                        length = len(dir + direction)
                        minlen = min(minlen, dist + cnt)
                        res += (dir + direction, dist + cnt),
                        
                if (ny, nx) in visit:
                    continue
                visit.add((ny, nx))
                q += (ny, nx, dir + direction, dist + cnt),
        
        res = [r[0] for r in res if r[1] == minlen]
        res.sort()
        return res[0] if res else 'impossible'


stime = time.time()
print('lul' == Solution().findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]))
print("impossible" == Solution().findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [0,0], [1,1]))
print('elapse time: {} sec'.format(time.time() - stime))