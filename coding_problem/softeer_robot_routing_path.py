import sys
import collections


H, W = 9, 14

input_grid = [
    '.......###....',
    '.........#....',
    '.#####...###..',
    '.#.........#..',
    '.#.#####...###',
    '.#.#...#.....#',
    '.###.###.....#',
    '.....#.......#',
    '.....#########',
]

grid = []
start_pos = []
num_cell = 0

for line in input_grid:
    grid += list(line),
    num_cell += line.count('#')

rows = len(grid)
cols = len(grid[0])

for y in range(rows):
    for x in range(cols):
        if grid[y][x] == '#':
            start_pos += (y, x),

# 0: N, 1: S, 2: W, 3: E
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
path = {
    (0, 1): 'RR',
    (0, 2): 'L',
    (0, 3): 'R',
    (1, 0): 'RR',
    (1, 2): 'R',
    (1, 3): 'L',
    (2, 0): 'R',
    (2, 1): 'L',
    (2, 3): 'RR',
    (3, 0): 'L',
    (3, 1): 'R',
    (3, 2): 'RR'
}

class MnCtx:
    def __init__(self):
        self.mn = float('inf')
        self.mn_trace = ''
        self.msy = -1
        self.msx = -1
        self.dir = -1

mn_ctx = MnCtx()


def dfs(y, x, cnt, d, trace, visited, mn_ctx):
    if cnt >= num_cell:
        if len(trace) < mn_ctx.mn:
            mn_ctx.mn = len(trace)
            mn_ctx.mn_trace = trace
        return

    for nd in range(4):
        ny = y + dirs[nd][0]
        nx = x + dirs[nd][1]
        dny = y + dirs[nd][0]*2
        dnx = x + dirs[nd][1]*2

        if (not (0 <= dny < rows and 0 <= dnx < cols)) or \
            (ny, nx) in visited or (dny, dnx) in visited:
            continue

        if grid[ny][nx] != '#' or grid[dny][dnx] != '#':
            continue

        rotate = ''
        if (d, nd) in path:
            rotate = path[(d, nd)]

        visited.add((ny, nx))
        visited.add((dny, dnx))
        dfs(dny, dnx, cnt + 2, nd, trace + rotate + 'A', visited, mn_ctx)
        visited.discard((ny, nx))
        visited.discard((dny, dnx))

for y, x in start_pos:
    for d, face in enumerate(['^', 'v', '<', '>']):
        visited = set()
        visited.add((y, x))
        pre_mn = mn_ctx.mn
        dfs(y, x, 1, d, face, visited, mn_ctx)
        if pre_mn > mn_ctx.mn:
            mn_ctx.msy = y
            mn_ctx.msx = x

print(mn_ctx.msy + 1, mn_ctx.msx + 1)
print(mn_ctx.mn_trace[:1])
print(mn_ctx.mn_trace[1:])
