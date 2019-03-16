
INF = 0xEFFFFFFF

dist = [
    #1,  2,  3,  4,  5
    [0,  10, 15, 20, 7],
    [10, 0,  10, 7,  10],
    [10, 0,  12, 16, 21],
    [20, 7,  16, 5,  9],
    [7,  10, 21, 9,  8]
]

def shortest_path(path, visited, cur_len, n):
    if len(path) == n:
        return cur_len + dist[path[0]][path[len(path)-1]]
    ret = INF
    for next in range(n):
        if visited[next]:
            continue
        if len(path) > 0:
            here = path[len(path)-1]
        else:
            here = 0
        path.append(next)
        print(next, end=' -> ')
        visited[next] = True
        cand = shortest_path(path, visited, cur_len + dist[here][next], n)
        ret = min(ret, cand)
        visited[next] = False
        path.pop(len(path)-1)
    return ret

path = []
n = 5
visited = [0 for i in range(n)]
print(shortest_path(path, visited, 0, n))
