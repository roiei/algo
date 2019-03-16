

graph = [
    [0, 2, 4, 3],
    [1, 0, 1, 5],
    [6, 3, 0, -2],
    [2 ,4, 5, 0],
]

cache = {}
def tsp_m(graph, pnode, nodes, start):
    idx = ''
    for i in nodes:
        idx += i
    if idx in cache:
        return None, cache[idx]

    cur_weight = graph[ord(pnode)-ord('A')][ord(nodes[0])-ord('A')]
    if -2 == cur_weight:
        return None, -2

    if 1 == len(nodes):
        path = []
        path.append(nodes[0])
        return path, cur_weight + graph[ord(nodes[0])-ord('A')][ord(start)-ord('A')]

    paths = []
    res = []
    pnode = nodes[0]
    nodes.pop(0)
    for i in range(len(nodes)):
        sub_nodes = []
        sub_nodes.append(nodes[i])
        sub_nodes.extend(nodes[:i])
        sub_nodes.extend(nodes[i+1:])
        path, ret = tsp_m(graph, pnode, sub_nodes, start)
        if -2 != ret:
            paths.append(path)
            res.append(ret)
    if res:
        min_res = min(res)
        min_path = paths[res.index(min_res)]
    else:
        min_res = -2
    if -2 == min_res:
        return None, -2

    if min_path:
        min_path.extend(pnode)
    cache[idx] = min_res + cur_weight
    return min_path, cache[idx]


start = 'A'
nodes = ['A', 'B', 'C', 'D']
path, res = tsp_m(graph, start, nodes, start)
path.reverse()
path.append(start)
print('cost = {} of path = {}'.format(res, path))
for k, v in cache.items():
    print('{}:{}'.format(k, v))
