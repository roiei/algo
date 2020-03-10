
import time
import copy
import collections


class Solution:
    def minimumMoves(self, grid: [[int]]) -> int:
        n = len(grid)
        q = [(0, 0, 0, 0, 1)]
        seen = set()

        while q:
            cnt, y, x, ey, ex = q.pop(0)
            if y == ey == n - 1 and x == n - 2 and ex == n - 1:
                return cnt
            
            if y == ey: # horizontal
                # down
                if y + 1 < n and grid[y + 1][x] == 0 and grid[ey + 1][ex] == 0:
                    if (y + 1, x, ey + 1, ex) not in seen:
                        q += (cnt + 1, y + 1, x, ey + 1, ex),
                        seen.add((y + 1, x, ey + 1, ex))
                # right
                if ex + 1 < n and grid[y][ex + 1] == 0:
                    if (y, x + 1, ey, ex + 1) not in seen:
                        q += (cnt + 1, y, x + 1, ey, ex + 1),
                        seen.add((y, x + 1, ey, ex + 1))
                # rotate
                if y + 1 < n and grid[y + 1][x] == 0 and grid[ey + 1][ex] == 0:
                    if (y, x, ey + 1, ex - 1) not in seen:
                        q += (cnt + 1, y, x, ey + 1, ex - 1),
                        seen.add((y, x, ey + 1, ex - 1))
                
            else:       # vertical
                # down
                if ey + 1 < n and grid[ey + 1][x] == 0:
                    if (y + 1, x, ey + 1, ex) not in seen:
                        q += (cnt + 1, y + 1, x, ey + 1, ex),
                        seen.add((y + 1, x, ey + 1, ex))
                # right
                if x + 1 < n and grid[y][x + 1] == 0 and grid[ey][x + 1] == 0:
                    if (y, x + 1, ey, ex + 1) not in seen:
                        q += (cnt + 1, y, x + 1, ey, ex + 1),
                        seen.add((y, x + 1, ey, ex + 1))
                # rotate
                if x + 1 < n and grid[y][x + 1] == 0 and grid[ey][ex + 1] == 0:
                    if (y, x, ey - 1, ex + 1) not in seen:
                        q += (cnt + 1, y, x, ey - 1, ex + 1),
                        seen.add((y, x, ey - 1, ex + 1))
        
        return -1
        



stime = time.time()
print(11 == Solution().minimumMoves(
              [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]))
print('elapse time: {} sec'.format(time.time() - stime))