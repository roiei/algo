#from collections import deque
import collections


def dfs(g, visited, u):
    visited.add(u)
    print('visit = ', u)

    if u not in g:
        return

    for v in g[u]:
        if v in visited:
            continue
        dfs(g, visited, v)


def dfs2(g, visited, u):
    q = [u]
    visited = {u}

    while q:
        u = q.pop()
        print('visit = ', u)

        if u not in g:
            continue

        for v in g[u]:
            if v in visited:
                continue

            visited.add(v)
            q.append(v)


def bfs(g, visited, u):
    q = collections.deque([u])
    visited = {u}

    while q:
        u = q.popleft()

        print('visit = ', u)

        if u not in g:
            continue

        for v in g[u]:
            if v in visited:
                continue

            visited.add(v)
            q.append(v)


links = [[1, 2], [1, 3], [3, 5], [1, 4], [4, 6]]

g = {}
for u, v in links:
    if u not in g:
        g[u] = []
    g[u].append(v)

visited = set()

#dfs(g, visited, 1)
dfs(g, visited, 1)

