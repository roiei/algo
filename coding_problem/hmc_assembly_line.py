

N = 2
A, B, AB, BA = 1, 3, 1, 2
AN, BN = 10, 2

lines = [[1, 2, 1, 2], [1, 2, 1, 2]]


grid = [[0]*2 for _ in range(N)]
tran = [[0]*2 for _ in range(N)]

for i in range(N - 1):
    #A, B, AB, BA = map(int, sys.stdin.readline().split())
    A, B, AB, BA = lines[i]
    grid[i][0] = A
    grid[i][1] = B
    tran[i][0] = AB
    tran[i][1] = BA

#AN, BN = map(int, sys.stdin.readline().split())

grid[-1][0] = AN
grid[-1][1] = BN

for i in range(N - 1):
    grid[i + 1][0] += min(grid[i][0], grid[i][1] + tran[i][1])
    grid[i + 1][1] += min(grid[i][0] + tran[i][0], grid[i][1])

print(min(grid[-1]))