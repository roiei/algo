import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph):
        n = len(graph)
        trace = {}
        for i in range(n - 2, -1, -1):
            trace[i] = []
            for j in range(len(graph[i])):
                if graph[i][j] == n - 1:
                    trace[i].append([i, n - 1])
                    continue
                if graph[i][j] in trace:
                    for k in trace[graph[i][j]]:
                        trace[i].append([i] + k)
        return trace[0]

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = {}
        
        for u in range(n - 2, -1, -1):
            paths[u] = []
            
            for v in graph[u]:
                if v not in paths:
                    paths[u] += [u, v],
                    continue

                for path in paths[v]:
                    paths[u] += [u] + path,
        
        return paths[0]

    def get_all_paths(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        q = [(0, [0])]
        res = []

        while q:
            u, trace = q.pop(0)

            for v in graph[u]:
                q += (v, trace + [v]),

            if u == n - 1:
                res += trace,

        return res


stime = time.time()
print([[0, 3], [0, 1, 3], [0, 2, 3], [0, 1, 2, 3]] == Solution().allPathsSourceTarget(graph = [[1,2,3],[2,3],[3],[]]))
print('elapse time: {} sec'.format(time.time() - stime))