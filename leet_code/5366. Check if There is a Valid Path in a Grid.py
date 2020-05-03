
import time
import copy
import collections


class Solution:
    def hasValidPath(self, grid: [[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        sy, sx = 0, 0

        q = [(sy, sx)]
        visited = {(sy, sx)}

        coords = {1 : ('left', 'right'), 2 : ('up', 'down'), \
            3 : ('left', 'down'), 4 : ('right', 'down'), \
            5 : ('left', 'up'), 6 : ('right', 'up')}
        match = {'down' : 'up', 'up' : 'down', 'left' : 'right', 'right' : 'left'}

        while q:
            y, x = q.pop(0)
            if y == m - 1 and x == n - 1:
                return True

            fro, to = coords[grid[y][x]]
            adj_coords = None

            if fro + '-' + to == 'left-right':
                adj_coords = [(0, 1), (0, -1)]
            elif fro + '-' + to == 'up-down':
                adj_coords = [(1, 0), (-1, 0)]
            elif fro + '-' + to == 'left-down':
                adj_coords = [(1, 0), (0, -1)]
            elif fro + '-' + to == 'right-down':
                adj_coords = [(1, 0), (0, 1)]
            elif fro + '-' + to == 'left-up':
                adj_coords = [(-1, 0), (0, -1)]
            elif fro + '-' + to == 'right-up':
                adj_coords = [(-1, 0), (0, 1)]

            for oy, ox in adj_coords:
                ny = y + oy
                nx = x + ox

                if (ny, nx) in visited:
                    continue

                if not (0 <= ny < m and 0 <= nx < n):
                    continue

                nfrom, nto = coords[grid[ny][nx]]

                if not (match[to] == nfrom or match[to] == nto or \
                    match[fro] == nto or match[fro] == nfrom):
                    continue

                visited.add((ny, nx))
                q += (ny, nx),

        return False


stime = time.time()
print(True == Solution().hasValidPath(grid = [[2,4,3],[6,5,2]]))
print(False == Solution().hasValidPath(grid = [[1,2,1],[1,2,1]]))
print(False == Solution().hasValidPath(grid = [[1,1,2]]))
print(True == Solution().hasValidPath(grid = [[1,1,1,1,1,1,3]]))
print(True == Solution().hasValidPath(grid = [[2],[2],[2],[2],[2],[2],[6]]))
print('elapse time: {} sec'.format(time.time() - stime))