
# line = sys.stdin.readline()



n = 3
T = 3

signals = [[2, 6, 12, 9],
[7, 1, 11, 6],
[6, 3, 5, 11],
[1, 1, 12, 9],
[3, 11, 8, 2],
[1, 7, 11, 9],
[4, 6, 2, 3],
[2, 4, 2, 4],
[6, 9, 2, 6]]



inters = [[[0]*4 for x in range(n)] for y in range(n)]
print(inters)


rows = len(signals)
cols = len(signals[0])

for iidx in range(rows):
    y = iidx//n
    x = iidx%n
    for t in range(cols):
        inters[y][x][t] = signals[iidx][t]



signal_ways = {
    1: [(0, 1), [(-1, 0), (0, 1), (1, 0)]],
    2: [(-1, 0), [(0, -1), (-1, 0), (0, 1)]],
    3: [(0, -1), [(-1, 0), (0, -1), (1, 0)]],
    4: [(1, 0), [(0, -1), (1, 0), (0, 1)]],
    5: [(0, 1), [(-1, 0), (0, 1)]],
    6: [(-1, 0), [(0, -1), (-1, 0)]],
    7: [(0, -1), [(0, -1), (1, 0)]],
    8: [(1, 0), [(1, 0), (0, 1)]],
    9:  [(0, 1), [(0, 1), (1, 0)]],
    10: [(-1, 0), [(-1, 0), (0, 1)]],
    11: [(0, -1), [(-1, 0), (0, -1)]],
    12: [(1, 0), [(0, -1), (1, 0)]]
}
       

def dfs(y, x, t, dir):
    if t == T:
        return 1

    sig_num = inters[y][x][t]
    valid_dir, next_coords = signal_ways[sig_num]

    if dir != valid_dir:
        return 1

    cnt = 1
    for oy, ox in next_coords:
        if not (0 <= y + oy < n and 0 <= x + ox < n):
            continue

        cnt += dfs(y + oy, x + ox, t + 1, (oy, ox))

    return cnt

cnt = dfs(0, 0, 0, (-1, 0))
print('cnt = ', cnt)



