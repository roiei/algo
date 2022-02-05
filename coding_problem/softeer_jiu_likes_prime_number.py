import copy
import sys
import collections
import heapq
import math



N, M = 10, 13
edges = [
    [1, 2, 5],
    [1, 3, 1],
    [1, 4, 2],
    [2, 5, 5],
    [3, 5, 4],
    [3, 6, 1],
    [4, 6, 1],
    [4, 7, 3],
    [5, 8, 5],
    [6, 9, 4],
    [7, 9, 2],
    [8, 10, 5],
    [9, 10, 3]
]


g = collections.defaultdict(list)

for u, v, w in edges:
    g[u] += (v, w),
    g[v] += (u, w),


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False

    return True


def do_dijkstra():
    q = [(0, 1)]        # cost, node
    mn_costs = [float('inf')]*(N + 1)
    mn_costs[1] = 0

    while q:
        cost, u = heapq.heappop(q)
        if cost > mn_costs[u]:
            continue

        for v, vcost in g[u]:
            mx_cost = max(vcost, cost)

            if mx_cost < mn_costs[v]:
                mn_costs[v] = mx_cost
                heapq.heappush(q, (mx_cost, v))

    return mn_costs[-1]


mn_level = do_dijkstra() + 1

while True:
    if is_prime(mn_level):
        break

    mn_level += 1

print(mn_level)