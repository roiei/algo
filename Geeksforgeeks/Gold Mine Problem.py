

def get_max(grid):
    rows = len(grid)
    cols = len(grid[0])

    if 1 == rows:
        for x in range(1, cols):
            grid[0][x] += grid[0][x-1]
        return grid[0][-1]
    if 1 == cols:
        return max([grid[y][0] for y in range(rows)])

    for x in range(1, cols):
        for y in range(rows):
            if 0 == y:
                grid[y][x] += max(grid[y][x-1], grid[y+1][x-1])
            elif rows-1 == y:
                grid[y][x] += max(grid[y-1][x-1], grid[y][x-1])
            else:
                grid[y][x] += max(grid[y-1][x-1], grid[y][x-1], grid[y+1][x-1])
    return max([grid[y][-1] for y in range(rows)])


matrix = [77,15,93,35,86,92,49,
          21,62,27,90,59,63,26,
          40,26,72,36,11,68,67,
          29,82,30,62,23,67,35]
m, n = 4, 7
grid = [[0]*n for y in range(m)]
for y in range(m):
    for x in range(n):
        grid[y][x] = matrix[y*n + x]

res = get_max(grid)
print(res)


# tc = int(input())
# for t in range(tc):
#     m, n = list(map(int, input().split()))
#     matrix = list(map(int, input().split()))
#     grid = [[0]*n for y in range(m)]
#     for y in range(m):
#         for x in range(n):
#             grid[y][x] = matrix[y*n + x]
#     res = get_max(grid)
#     print(res)