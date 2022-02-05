

N, M = 8, 9
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,1,1,0],
    [0,1,0,1,1,1,0,1,0],
    [0,1,0,0,1,0,0,1,0],
    [0,1,0,1,1,1,0,1,0],
    [0,1,1,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0]
]


def fill_outside(grid):
    q = [(0, 0)]    # regard 0, 0 is empty cell

    while q:
        y, x = q.pop(0)
        grid[y][x] = 2

        for oy, ox in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny = y + oy
            nx = x + ox
            if not (0 <= ny < N and 0 <= nx < M):
                continue

            if 2 == grid[ny][nx] or 1 == grid[ny][nx]:
                continue

            q += (ny, nx),

def erode(grid):
    candidates = []
    q = [(0, 0)]
    visited = set()
    visited.add((0, 0))

    while q:
        y, x = q.pop(0)

        for oy, ox in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny = y + oy
            nx = x + ox

            if not (0 <= ny < N and 0 <= nx < M):
                continue

            if (ny, nx) in visited:
                continue

            if 2 == grid[ny][nx]:
                q += (ny, nx),
                visited.add((ny, nx))

            if 1 != grid[ny][nx]:
                continue

            out_cnt = 0
            for ay, ax in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                adjy = ny + ay
                adjx = nx + ax

                if not (0 <= adjy < N and 0 <= adjx < M):
                    continue

                if 2 == grid[adjy][adjx]:
                    out_cnt += 1

            if out_cnt >= 2:
                candidates += (ny, nx),

    num_erode = len(candidates) if candidates else 0
    while candidates:
        y, x = candidates.pop(0)
        grid[y][x] = 2

    return num_erode


fill_outside(grid)
cnt = 0

while True:
    num_erode = erode(grid)
    if not num_erode:
        break

    cnt += 1

print(cnt)

