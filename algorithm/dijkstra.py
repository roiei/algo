import collections


class NodeState(object):
    def __init__(self):
        self.parent = None
        self.distance = 0       # 0 == INF


def shortest_dijkstra(links, cur):
    vertices = []
    g = collections.defaultdict(dict)
    for u, v, w in links:
        g[u][v] = w
        if u not in vertices:
            vertices += u,

    visited = set()
    state = {}

    for kind in vertices:
        state[kind] = NodeState()
        state[kind].parent = cur if kind != cur else None
        state[kind].distance = 0

    adj_max_dist = 0
    for adj, w in g[cur].items():
        state[adj].distance = g[cur][adj]   # distance = edge's weight, at first
        if adj_max_dist < g[cur][adj]:
            adj_max_dist = g[cur][adj] + 1

    state[cur].distance = adj_max_dist
    visited.add(cur)
    q = [cur]

    while q:
        cur = q.pop(0)

        for v in vertices:
            if (v not in visited
                and state[v].distance > 0 
                and state[cur].distance > state[v].distance):

                visited.add(v)
                q += v,

                for adj, w in g[v].items():
                    if adj in visited:
                        continue

                    dist = state[v].distance + w
                    if state[adj].distance == 0 or dist < state[adj].distance:
                        state[adj].distance = dist
                        state[adj].parent = v

    for v in vertices:
        if state[v].parent != None:
            print('{} -- {} --> {}'.format(state[v].parent, state[v].distance, v))


links = [
 ('A', 'C', 1),('A', 'B', 4),('A', 'D', 2),
 ('A', 'E', 3),('C', 'D', 2),('D', 'F', 4),
 ('B', 'F', 4),('E', 'F', 4),('D', 'G', 4),
 ('G', 'H', 3),('G', 'I', 3),('G', 'J', 4),
 ('H', 'I', 2),('I', 'J', 2),('F', 'J', 2),
 ('J', 'K', 1),('F', 'K', 4)]

shortest_dijkstra(links, 'A')