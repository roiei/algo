
nodes = [1, 2, 3, 4]
graph = [
    [0, 10, 15, 20],
    [5, 0,  9,  10],
    [6, 13, 0,  12],
    [8 ,8,  9,  0],
]


# nodes = [1, 2, 3, 4, 5]
# graph = [
#     [0, 10, 15, 20, 7],
#     [5, 0,  9,  10, 5],
#     [6, 13, 0,  12, 9],
#     [8 ,8,  9,  0,  4],
#     [1, 2,  5,  10, 0]
# ]

cache = {}
def tsp_m(graph, pnode, nodes, start):
    idx = ''
    for i in nodes:
        idx += str(i)
    if idx in cache:
        print(idx, ' : ', cache[idx])
        return cache[idx]
    cur_weight = graph[pnode-1][nodes[0]-1]
    #print('{} -- {} --> {}'.format(pnode, cur_weight, nodes[0]))
    if (pnode != nodes[0] and 0 == cur_weight):
        return -2   # no cyclic path
    if 1 == len(nodes):
        return cur_weight + graph[nodes[0]-1][start-1]
    res = []
    pnode = nodes[0]
    nodes.pop(0)
    for i in range(len(nodes)):
        sub_nodes = []
        sub_nodes.append(nodes[i])
        sub_nodes.extend(nodes[:i])
        sub_nodes.extend(nodes[i+1:])
        ret = tsp_m(graph, pnode, sub_nodes, start)
        if -2 != ret:
            res.append(ret)
    if not res:
        return -2   # no sub path
    cache[idx] = min(res) + cur_weight
    return cache[idx]


import sys


start = 1

# n = int(sys.stdin.readline())
# nodes = [i+1 for i in range(n)]
# graph = []
# for i in range(n):
#     line = list(map(int, sys.stdin.readline().split()))
#     graph.append(line)

res = tsp_m(graph, start, nodes, start)


print('{}'.format(res))


# for k, v in cache.items():
#     print('{}:{}'.format(k, v))
