import collections
import sys


K, N = map(int, sys.stdin.readline().split())
grid = []
tran = []

for i in range(N - 1):
    line = list(map(int, sys.stdin.readline().split()))
    grid += line[:K],
    tran += line[K],

line = list(map(int, sys.stdin.readline().split()))
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