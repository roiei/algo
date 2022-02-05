import heapq
from collections import defaultdict



edges = [[1, 2, 4], [1, 3, 2], [2, 5, 3], [3, 4, 1], [4, 5, 3], [4, 6, 5], [5, 7, 4], [6, 7, 5]]
g = defaultdict(lambda: defaultdict(int))

for u, v, w in edges:
    g[u][v] = w

start = 1
end = 7

def get_shortest_cost(g, start, end):
    q = [(0, start, [start])]

    while q:
        total, u, trace = heapq.heappop(q)
        if u == end:
            return total, trace

        for v, w in g[u].items():
            heapq.heappush(q, (total + w, v, trace + [v]))

    return -1, None


cost, trace = get_shortest_cost(g, start, end)
print('shortest cost = ', cost)
print('trace = ', trace)


def dijkstra(g, start):
    dists = defaultdict(lambda: float('inf'))
    dists[start] = 0
    q = [(0, start, [start])]

    while q:
        dist, u, trace = heapq.heappop(q)

        if dists[u] < dist:
            continue

        for v, w in g[u].items():
            if dist + w < dists[v]:
                print('dists[{}] = {}, trace = {}'.format(v, dist + w, trace + [v]))
                dists[v] = dist + w
                heapq.heappush(q, (dist + w, v, trace + [v]))

    return dists

dists = dijkstra(g, start)
print('dists = ', dists)

