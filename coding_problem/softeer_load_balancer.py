import sys

import collections


lines = [
    [8, 6],
    [3,2,5,8],
    [0],
    [0],
    [0],
    [3,2,4,3],
    [0],
    [0],
    [2,6,7]
]

def get_line():
    n = len(lines)
    for _ in range(n):
        yield lines[_]

gen = get_line()

g = collections.defaultdict(list)
N, K = next(gen)
for i in range(1, N + 1):
    vals = next(gen)
    if 0 == vals[0]:
        pass

    for adj in vals[1:]:
        #if adj in g[i]:  <- duplicated edge exists ! in some TC
        #    continue

        g[i] += adj,


# g = collections.defaultdict(list)
# N, K = map(int, sys.stdin.readline().split())
# for i in range(1, N + 1):
#     vals = list(map(int, sys.stdin.readline().split()))
#     if 0 == vals[0]:
#         pass

#     for adj in vals[1:]:
#         if adj in g[i]:
#             continue

#         g[i] += adj,


def sort_topo(g, N):
    indegree = [0]*(N + 1)

    for u, adjs in g.items():
        for v in adjs:
            indegree[v] += 1

    q = [1]
    order = []

    while q:
        u = q.pop(0)
        order += u,

        for adj in g[u]:
            indegree[adj] -= 1
            if indegree[adj] == 0:
                q += adj,

    return order


def calc(g, order, N, K):
    loads = collections.defaultdict(int)
    loads[1] = K

    for u in order:
        num_adj = len(g[u])
        if 0 == num_adj:
            continue

        quo = loads[u]//num_adj
        rem = loads[u]%num_adj

        for adj in g[u]:
            loads[adj] += quo

        for adj in g[u]:
            if rem == 0:
                break

            loads[adj] += 1
            rem -= 1

    return loads


order = sort_topo(g, N)

loads = calc(g, order, N, K)

loads = sorted(loads.items(), key=lambda p: p[0])
loads = [num for node, num in loads]
print(' '.join(map(str, loads)))
