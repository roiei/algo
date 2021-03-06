

class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        trace = {}
        for i in range(n-2, -1, -1):
            trace[i] = []
            for j in range(len(graph[i])):
                if graph[i][j] == n-1:
                    trace[i].append([i, n-1])
                    continue
                if graph[i][j] in trace:
                    for k in trace[graph[i][j]]:
                        trace[i].append([i] + k)
        return trace[0]

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = {}
        
        for u in range(n-2, -1, -1):
            paths[u] = []
            
            for v in graph[u]:
                if v not in paths:
                    paths[u] += [u, v],
                    continue

                for path in paths[v]:
                    paths[u] += [u] + path,
        
        return paths[0]
