import copy
import sys


N = 2
grid = [
    [1, 1],
    [2, 2],
    [1, 1],
    [3, 3],
    [4, 4],
    [1, 2]
]


N = 3
grid = [
    [8, 5, 1],
    [9, 6, 1],
    [10, 7, 1],
    [11, 1, 3],
    [12, 1, 3],
    [13, 1, 3],
    [1, 2, 2],
    [1, 2, 2],
    [1, 2, 2]
]


rows = len(grid)
cols = len(grid[0])


class Rect:
    def __init__(self):
        self.mnx = float('inf')
        self.mny = float('inf')
        self.mxx = 0
        self.mxy = 0


def remove_values(grid, y, x, val, removed_coord, rect):
    if '.' == grid[y][x] or val != grid[y][x]:
        return 0

    visited = set()
    cnt = 1
    q = [(y, x)]
    visited.add((y, x))

    while q:
        y, x = q.pop(0)
        grid[y][x] = '.'
        removed_coord.add((y, x))
        
        rect.mnx = min(rect.mnx, x)
        rect.mny = min(rect.mny, y)
        rect.mxx = max(rect.mxx, x)
        rect.mxy = max(rect.mxy, y)

        for oy, ox in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
            if not (rows - N <= oy < rows and cols - N <= ox < cols):
                continue

            if '.' == grid[oy][ox] or (oy, ox) in visited or val != grid[oy][ox]:
                continue

            q += (oy, ox),
            visited.add((oy, ox))
            cnt += 1

    return cnt


def arrange_grid(grid):
    for x in range(cols):
        ny = rows - 1
        for y in range(rows - 1, -1, -1):
            if '.' == grid[y][x]:
                continue

            grid[ny][x] = grid[y][x]
            ny -= 1

        for y in range(ny + 1):
            grid[y][x] = '.'


def dfs(cnt, score, grid, mx):
    if mx[cnt] >= score:
        #print(mx[cnt], score)
        return

    if 3 == cnt:
        mx[cnt] = max(mx[0], score)
        return

    visited = set()

    for y in range(rows - N, rows):
        for x in range(cols - N, cols):
            if (y, x) in visited:
                continue

            rect = Rect()
            ngrid = copy.deepcopy(grid)
            removed_coord = set()
            num_removed = remove_values(ngrid, y, x, ngrid[y][x], removed_coord, rect)

            area_size = 0
            if removed_coord:
                area_size = (rect.mxy - rect.mny + 1)*(rect.mxx - rect.mnx + 1)

            if removed_coord:
                visited |= removed_coord

            arrange_grid(ngrid)
            dfs(cnt + 1, score + num_removed + area_size, ngrid, mx)


mx = [float('-inf')]*4
dfs(0, 0, grid, mx)
print(max(mx))
