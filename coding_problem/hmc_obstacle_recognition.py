N = 7
grid = [
    [1,1,1,0,1,1,1],
    [0,1,1,0,1,0,1],
    [0,1,1,0,1,0,1],
    [0,0,0,0,1,0,0],
    [0,1,1,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,0,0,0,0]
]


grid = []
N = int(sys.stdin.readline())
for _ in range(N):
    line = str(sys.stdin.readline()).strip()
    line = list(line)
    line = list(map(int, line))
    grid += line,



def dfs(y, x):
    if 0 == grid[y][x]:
        return 0

    cnt = 1
    grid[y][x] = 0

    for oy, ox in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = oy + y, ox + x
        if not (0 <= ny < N and 0 <= nx < N):
            continue

        cnt += dfs(ny, nx)

    return cnt


cnts = []
for y in range(N):
    for x in range(N):
        if 1 == grid[y][x]:
            cnts += dfs(y, x),

cnts.sort()
print(len(cnts))
for cnt in cnts:
    print(cnt)