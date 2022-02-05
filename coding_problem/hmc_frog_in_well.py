import collections


N, M = 5, 3
weights = [1,2,3,4,5]
relations = [
    [1, 3],
    [2, 4],
    [2, 5],
]


N, M = 5, 3
weights = [7, 5, 7, 7, 1]
relations = [
    [1, 2],
    [2, 3],
    [3, 4],
]


g = collections.defaultdict(dict)

for u, v in relations:
    g[u][v] = 1
    g[v][u] = 1

visited = set()
cnt = 0

for node in range(1, N + 1):
    val = weights[node - 1]
    if len(g[node].items()) == 0:
        cnt += 1
        continue

    for v, w in g[node].items():
        if val <= weights[v - 1]:
            break
    else:
        cnt += 1

print(cnt)