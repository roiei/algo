import time
from util_list import *
from util_tree import *
import collections


class Solution:
    def sumOfDistancesInTree_es(self, N, edges):
        if not edges:
            return [0]
        graph = [[0 for i in range(N)] for j in range(N)]
        visit = [False for i in range(N)]
        for edge in edges:
            graph[edge[0]][edge[1]] = 1
            graph[edge[1]][edge[0]] = 1 # undirected

        res = []
        for i in range(N):
            visit = [False for i in range(N)]
            dist = 1
            tot = 0
            q = [[i, 0]]
            while q:
                cur, dist = q.pop(0)
                tot += dist
                visit[cur] = True
                for j in range(len(graph[cur])):
                    if 0 != graph[cur][j] and False == visit[j]:
                        q.append([j, dist+1])
            res.append(tot)
        return res

    def dfs_count(self, cur, pre, graph, count, dist):
        for child in graph[cur]:
            if child == pre:
                continue
            self.dfs_count(child, cur, graph, count, dist)
            count[cur] += count[child]
            dist[cur] += count[child] + dist[child]

    def dfs_dist(self, cur, pre, graph, count, dist, N):
        for child in graph[cur]:
            if child == pre:
                continue
            dist[child] = dist[cur] - count[child] + (N - count[child])
            self.dfs_dist(child, cur, graph, count, dist, N)

    def sumOfDistancesInTree(self, N, edges):
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        count = [1]*N
        dist = [0]*N
        self.dfs_count(0, None, graph, count, dist)
        self.dfs_dist(0, None, graph, count, dist, N)
        return dist


stime = time.time()
print([8,12,6,10,10,10] == Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
print('elapse time: {} sec'.format(time.time() - stime))
