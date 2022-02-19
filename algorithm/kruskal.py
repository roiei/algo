import collections


links = [
    ['A', 'B', 2],
    ['A', 'B', 4],
    ['B', 'C', 3],
    ['B', 'D', 5],
    ['C', 'D', 7],
    ['C', 'G', 3],
    ['G', 'E', 1],
    ['D', 'E', 2],
    ['F', 'E', 3],
    ['F', 'G', 4]
]


def get_root(group, key):
    while group[key] != key:
        key = group[key]

    return key


def kruskal_mcst():
    group = collections.defaultdict(int)
    q = []
    vertices = set()

    for u, v, w in links:
        q += (u, v, w),
        vertices.add(u)
        vertices.add(v)

    for i, vertex in enumerate(list(vertices)):
        group[vertex] = vertex

    q = collections.deque(sorted(q, key=lambda p: p[2]))
    live_edges = []

    while q:
        u, v, w = q.popleft()

        u_gid = get_root(group, u)
        v_gid = get_root(group, v)

        if u_gid != v_gid:
            group[v_gid] = u_gid
            live_edges += (u, v, w),

    return live_edges


live_edges = kruskal_mcst()

for u, v, w in live_edges:
    print(u, v, w)








    


