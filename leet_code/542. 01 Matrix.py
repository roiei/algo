import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def __init__(self):
        self.dirs = [[1, 0], [-1, 0], [0, +1], [0, -1]]

    def update(self, matrix, y, x, rows, cols, prev):
        if 0 == matrix[y][x] or (-1 != matrix[y][x] and prev+1 >= matrix[y][x]):
            return
        zeros = 0
        vals = []
        for dir in self.dirs:
            ny = y + dir[0]
            nx = x + dir[1]
            if 0 <= ny < rows and 0 <= nx < cols:
                if 0 == matrix[ny][nx]:
                    zeros += 1
                elif -1 != matrix[ny][nx]:
                    vals.append(matrix[ny][nx])
        if 0 < zeros:
            matrix[y][x] = 1
        elif vals:
            matrix[y][x] = 1 + min(vals)

        for dir in self.dirs:
            ny = y + dir[0]
            nx = x + dir[1]
            if (0 <= ny < rows) and (0 <= nx < cols):
                if 0 != matrix[ny][nx]:
                    self.update(matrix, ny, nx, rows, cols, matrix[y][x])

    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for y in range(rows):
            for x in range(cols):
                if 1 == matrix[y][x]:
                    matrix[y][x] = -1
        for y in range(rows):
            for x in range(cols):
                if 0 == matrix[y][x]:
                    if y < rows-1:
                        self.update(matrix, y+1, x, rows, cols, matrix[y][x])
                    if y > 0:
                        self.update(matrix, y-1, x, rows, cols, matrix[y][x])
                    if x < cols-1:
                        self.update(matrix, y, x+1, rows, cols, matrix[y][x])
                    if x > 0:
                        self.update(matrix, y, x-1, rows, cols, matrix[y][x])
        return matrix


    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        sources = [(y, x) for y in range(rows) for x in range(cols) if matrix[y][x] == 0]
        visit = [[False]*cols for _ in range(rows)]

        for coord in sources:
            visit[coord[0]][coord[1]] = True
        q = collections.deque([source+(0,) for source in sources])

        while (q):
            y, x, d = q.popleft()
            #print(y, x, d)

            matrix[y][x] = d

            for ny, nx in [(y+1, x), (y, x-1),(y, x+1), (y-1, x)]:
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                if visit[ny][nx] == False:
                    visit[ny][nx] = True
                    q.append((ny, nx) + (d + 1,))
        return matrix


     def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visit = [[False]*cols for _ in range(rows)]

        q = []
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] == 0:
                    visit[y][x] = True
                    q += (y, x, 0),

        while q:
            y, x, dist = q.pop(0)

            for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                if visit[ny][nx] == False:
                    visit[ny][nx] = True
                    matrix[ny][nx] = dist + 1
                    q += (ny, nx, dist + 1),

        return matrix


    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        visit = [[False]*cols for _ in range(rows)]

        q = collections.deque()
        for y in range(rows):
            for x in range(cols):
                if matrix[y][x] == 0:
                    visit[y][x] = True
                    q.append((y, x, 0))

        while q:
            y, x, dist = q.popleft()
            for ny, nx in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue
                if visit[ny][nx] == False:
                    visit[ny][nx] = True
                    matrix[ny][nx] = dist + 1
                    q.append((ny, nx, dist + 1))

        return matrix


stime = time.time()
# res = Solution().updateMatrix([
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]])
res = Solution().updateMatrix([
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]])
# res = Solution().updateMatrix([
#     [1, 1, 1], 
#     [1, 1, 0], 
#     [1, 0, 0]])
for r in res:
    print(r)
print('elapse time: {} sec'.format(time.time() - stime))