import collections


N, K = 5, 2
inputs = [
    [-4, -2, 1],
    [-5, -3, 1],
    [5, -4, 2],
    [4, -5, 2],
    [3, -8, 2]
]

# N, K = 5, 3
# inputs = [
#     [3, 7, 1],
#     [5, 8, 1],
#     [6, 5, 2],
#     [7, 1, 3],
#     [9, 3, 3]
# ]


# N, K = 7, 3
# inputs = [
#     [-4, 0, 1],
#     [-5, -1, 1],
#     [0, 43, 2],
#     [3, 23, 3],
#     [8, -19, 2],
#     [10, 0, 3],
#     [20, 0, 2]
# ]

# N, K = 3, 3
# inputs = [
#     [1, 1, 1],
#     [1, 1, 2],
#     [1, 1, 3],
# ]



coords = collections.defaultdict(set)
for x, y, k in inputs:
    coords[k].add((x, y))

k_coords = list(map(list, (sorted(coords.items(), key=lambda p: p[0]))))
n = len(k_coords)

for i in range(len(k_coords)):
    k_coords[i][1] = list(k_coords[i][1])


def dfs(k, seq, res):
    if k == n:
        res.add(tuple(seq))
        return

    for i in range(len(k_coords[k][1])):
        dfs(k + 1, seq + [k_coords[k][1][i]], res)


res = set()
dfs(0, [], res)
mn = float('inf')

for coords in res:
    mnx = mny = float('inf')
    mxx = mxy = float('-inf')

    for x, y in coords:
        mnx = min(mnx, x)
        mxx = max(mxx, x)
        mny = min(mny, y)
        mxy = max(mxy, y)

    mn = min(mn, (mxy - mny)*(mxx - mnx))

print(mn)
