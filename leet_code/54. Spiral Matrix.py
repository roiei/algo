import time


class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        trace = []
        height = len(matrix)
        width = len(matrix[0])
        marked = [[False for i in range(width)] for j in range(height)]

        offsetx = 0
        offsety = 0

        while offsetx < (width-offsetx) and offsety < (height-offsety):
            x = y = -1
            for x in range(offsetx, width-offsetx):
                if False == marked[offsety][x]:
                    trace.append(matrix[offsety][x])
                    marked[offsety][x] = True
            if -1 != x:
                for y in range(1+offsety, height-offsety):
                    if False == marked[y][x]:
                        trace.append(matrix[y][x])
                        marked[y][x] = True
            if -1 != y:
                for x in range(width-2-offsetx, offsetx-1, -1):
                    if False == marked[y][x]:
                        trace.append(matrix[y][x])
                        marked[y][x] = True
            for y in range(height-2-offsety, offsety, -1):
                if False == marked[y][x]:
                    trace.append(matrix[y][x])
                    marked[y][x] = True
            offsetx += 1
            offsety += 1
        return trace

    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if not matrix:
            return None

        rows = len(matrix)
        cols = len(matrix[0])
        
        q = [(0, 0)]
        visited = {(0, 0)}
        res = [matrix[0][0]]
        visited_start = set()
        
        while q:
            y, x = q.pop(0)
            visited_start.add((y, x))
            ny = y
            nx = x        
            
            for oy, ox in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                while (0 <= ny + oy < rows and 0 <= nx + ox < cols):
                    if (ny + oy, nx + ox) in visited:
                        break

                    ny += oy
                    nx += ox

                    visited.add((ny, nx))
                    res += matrix[ny][nx],

            if (ny, nx) not in visited_start:
                q += (ny, nx),

        return res


stime = time.time()
print([1,2,3,6,9,8,7,4,5] == Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print([2, 3] == Solution().spiralOrder([[2, 3]]))
print([7, 9, 6] == Solution().spiralOrder([[7],[9],[6]]))
print('elapse time: {} sec'.format(time.time() - stime))

