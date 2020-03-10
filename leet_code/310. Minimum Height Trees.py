import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
        if not n: return []
        conn = [[] for _ in range(n)]
        deg = [0 for _ in range(n)]
        for u, v in edges:
            conn[u].append(v)
            conn[v].append(u)
            deg[u] += 1
            deg[v] += 1

        leaves = [u for u in range(n) if deg[u] <= 1]
        done = set(leaves)

        while len(done) < n:
            nxt = []
            for u in leaves:
                for v in conn[u]:
                    if v in done:
                        continue
                    deg[v] -= 1
                    if deg[v] == 1:
                        done.add(v)
                        nxt.append(v)
            leaves = nxt
        return list(leaves)

    def findMinHeightTrees(self, n: int, edges: [[int]]) -> [int]:
        if 0 == n:
            return []
        if not edges:
            return [*range(n)]
        
        visit = [False]*n
        degree = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        
        for edge in edges:
            graph[edge[0]] += edge[1],
            degree[edge[0]] += 1
            graph[edge[1]] += edge[0],
            degree[edge[1]] += 1
        
        leaves = [k for k, v in degree.items() if v == 1]
        res = None
        while leaves:
            nleaves = []
            res = []
            for i in leaves:
                res += i,
                for j in graph[i]:
                    if j in nleaves:
                        continue
                    degree[j] -= 1
                    if 1 == degree[j]:
                        nleaves += j,
            leaves = nleaves
        return res


stime = time.time()
print(Solution().findMinHeightTrees(4, [[1, 0], [1, 2], [1, 3]]))
print('elapse time: {} sec'.format(time.time() - stime))

