rows, cols = 3, 3
grid = [
    ['H', '.', '*'],
    ['.', '.', '.'],
    ['W', '.', '.']
]

rows, cols = 4, 3
grid = [
    ['H', '.', '*'],
    ['.', '.', '.'],
    ['X', 'X', 'X'],
    ['W', '.', '.']
]


import sys

rows, cols = map(int, sys.stdin.readline().split())
grid = []
for _ in range(rows):
    grid += list(sys.stdin.readline()),


wq = []
wvisited = set()
rq = []
rvisited = set()

for y in range(rows):
    for x in range(cols):
        if 'W' == grid[y][x]:
            wq += (y, x),
            wvisited.add((y, x))
        elif '*' == grid[y][x]:
            rq += (y, x),
            rvisited.add((y, x))

cnt = 0

while wq:
    nrq = []
    while rq:
        ry, rx = rq.pop(0)

        for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = oy + ry
            nx = ox + rx

            if not (0 <= ny < rows and 0 <= nx < cols):
                continue

            if 'X' == grid[ny][nx] or 'H' == grid[ny][nx] or (ny, nx) in rvisited:
                continue

            rvisited.add((ny, nx))
            nrq += (ny, nx),

    rq = nrq

    nwq = []
    while wq:
        wy, wx = wq.pop(0)
        if 'H' == grid[wy][wx]:
            break

        for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = oy + wy
            nx = ox + wx

            if not (0 <= ny < rows and 0 <= nx < cols):
                continue

            if 'X' == grid[ny][nx] or (ny, nx) in rvisited:
                continue

            rvisited.add((ny, nx))
            nwq += (ny, nx),

    wq = nwq

    if 'H' == grid[wy][wx]:
        break

    cnt += 1


print(cnt if 'H' == grid[wy][wx] else 'FAIL')


       
    