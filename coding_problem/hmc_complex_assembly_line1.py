import collections
import sys


K, N = 2, 2
lines = [[1, 3, 1, 2]]
last_line = [10, 2]


grid = []
tran = []

for i in range(N - 1):
    #line = list(map(int, sys.stdin.readline().split()))
    line = lines[i]
    grid += line[:K],
    pos = 0
    tran_map = collections.defaultdict(int)

    for j in range(K):
        for k in range(K):
            if j == k:
                continue

            tran_map[(j, k)] = line[K + pos]
            pos += 1

    tran += tran_map,

#line = list(map(int, sys.stdin.readline().split()))
line = last_line
grid += line,

for i in range(N - 1):
    mn = min(grid[i])
    idx = grid[i].index(mn)

    for j in range(K):
        if j == idx:
            grid[i + 1][j] += mn
        else:
            grid[i + 1][j] += min(grid[i][j], mn + tran[i])

print(min(grid[-1]))