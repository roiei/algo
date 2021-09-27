import time
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]':
        ox = oy = 0
        matrix = [[0 for i in range(n)] for i in range(n)]
        cnt = 1
        while ox < (n-ox) and oy < (n-oy):
            for x in range(ox, n-ox):
                matrix[oy][x] = cnt; cnt += 1
            for y in range(oy+1, n-oy):
                matrix[y][x] = cnt; cnt += 1
            for x in range(n-ox-2, ox-1, -1):
                matrix[y][x] = cnt; cnt += 1
            for y in range(n-oy-2, oy, -1):
                matrix[y][x] = cnt; cnt += 1
            ox += 1
            oy += 1
        return matrix

    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return None

        rows = cols = n
        y = x = 0
        q = []
        matrix = [[0]*cols for y in range(rows)]
        cnt = 1

        while True:
            pre_len = len(q)

            for oy, ox in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (y, x) not in q:
                    q += (y, x),
                    matrix[y][x] = cnt
                    cnt += 1

                while 0 <= oy + y < rows and 0 <= ox + x < cols:
                    if (oy + y, ox + x) in q:
                        break
                    q += (oy + y, ox + x),
                    matrix[oy + y][ox + x] = cnt
                    cnt += 1
                    y += oy
                    x += ox

            if pre_len == len(q):
                break

        return matrix

    def generateMatrix(self, n: int) -> List[List[int]]:
        q = [(0, 0, 'right')]
        visited = {(0, 0)}
        
        grid = [[0]*n for _ in range(n)]
        cnt = 1

        while q:
            y, x, dir = q.pop(0)
            grid[y][x] = cnt
            cnt += 1
            
            if dir == 'right':
                if not x + 1 < n or (y, x + 1) in visited:
                    if y + 1 < n and (y + 1, x) not in visited:
                        dir = 'down'
                        y += 1
                else:
                    x += 1
            elif dir == 'down':
                if not y + 1 < n or (y + 1, x) in visited:
                    if x - 1 >= 0 and (y, x - 1) not in visited:
                        dir = 'left'
                        x -= 1
                else:
                    y += 1
            elif dir == 'left':
                if not x - 1 >= 0 or (y, x - 1) in visited:
                    if y - 1 >= 0 and (y - 1, x) not in visited:
                        dir = 'up'
                        y -= 1
                else:
                    x -= 1
            elif dir == 'up':
                if not y - 1 >= 0 or (y - 1, x) in visited:
                    if x + 1 < n and (y, x + 1) not in visited:
                        dir = 'right'
                        x += 1
                else:
                    y -= 1

            if (y, x) not in visited:
                visited.add((y, x))
                q += (y, x, dir),
        
        return grid

    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return None

        rows = cols = n
        visited = set()
        matrix = [[0]*cols for y in range(rows)]
        cnt = 1
        y = x = 0

        while True:
            pre_cnt = cnt

            for oy, ox in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (y, x) not in visited:
                    matrix[y][x] = cnt
                    visited.add((y, x))
                    cnt += 1

                while 0 <= oy + y < rows and 0 <= ox + x < cols and \
                    (oy + y, ox + x) not in visited:
                    
                    matrix[oy + y][ox + x] = cnt
                    visited.add((oy + y, ox + x))
                    y += oy
                    x += ox
                    cnt += 1

            if pre_cnt == cnt:
                break

        return matrix


stime = time.time()
print([[1, 2, 3], [8, 9, 4], [7, 6, 5]] == Solution().generateMatrix(3))
print([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]] == Solution().generateMatrix(4))
print([[1, 2], [4, 3]] == Solution().generateMatrix(2))
print([[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]] == Solution().generateMatrix(5))
print([[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]] == Solution().generateMatrix(6))
print('elapse time: {} sec'.format(time.time() - stime))