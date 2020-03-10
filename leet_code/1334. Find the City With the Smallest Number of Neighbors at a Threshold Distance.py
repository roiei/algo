
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:

    # Floyd
    def findTheCity(self, n, edges, maxd):
        dis = [[float('inf')] * n for _ in xrange(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in xrange(n):
            dis[i][i] = 0
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in xrange(n)}
        return res[min(res)]


    def findTheCity(self, n: int, edges: [[int]], distanceThreshold: int) -> int:
        
        g = collections.defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w

        cnt = float('inf')
        res = 0

        for i in range(n):
            visited = set()
            q = [(0, i)]

            while q:
                #if len(visited) == n:
                #    break

                weight, u = heapq.heappop(q)

                if u in visited or weight > distanceThreshold:
                    continue

                visited.add(u)   # DFS with min cost -> much as possible

                for v, w in g[u].items():
                    heapq.heappush(q, (weight + w, v))

            if len(visited) <= cnt:
                cnt = len(visited)
                res = i

        return res




            
stime = time.time()
#print(3 == Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
print(7 == Solution().findTheCity(8, [[3,5,9558],[1,2,1079],[1,3,8040],[0,1,9258],[4,7,7558],[5,6,8196],[3,4,7284],[1,5,6327],[0,4,5966],[3,6,8575],[2,5,8604],[1,7,7782],[4,6,2857],[3,7,2336],[0,6,6],[5,7,2870],[4,5,5055],[0,7,2904],[1,6,2458],[0,5,3399],[6,7,2202],[0,2,3996],[0,3,7495],[1,4,2262],[2,6,1390]], 7937))
print('elapse time: {} sec'.format(time.time() - stime))