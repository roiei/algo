import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def findCheapestPrice_ref(self, n, flights, src, dst, K):
        pq, g = [(0,src,K+1)], collections.defaultdict(dict)
        for s,d,c in flights: g[s][d] = c
        while pq:
            cost, s, k = heapq.heappop(pq)
            if s == dst: return cost
            if k:
                for d in g[s]:
                    heapq.heappush(pq, (cost+g[s][d], d, k-1))
        return -1


    def findCheapestPrice(self, n, flights, src, dst, K):
        graph = collections.defaultdict(dict)
        for u, v, weight in flights:
            graph[u][v] = weight

        visit = [False]*(len(flights)+1)
        q = [(0, src, K)]
        while q:
            weight, u, k = heapq.heappop(q)
            visit[u] = True
            if u == dst:
                return weight
            if k < 0:
                continue
            for v in graph[u].keys():
                if visit[v] == True:
                    continue
                heapq.heappush(q, (weight + graph[u][v], v, k-1))
        return -1


    def findCheapestPrice(self, n, flights, src, dst, K):
        g = collections.defaultdict(dict)
        for u, v, weight in flights:
            g[u][v] = weight
        
        visit = set()
        q = [(0, src, K)]
        while q:
            weight, node, k = heapq.heappop(q)
            visit.add(node)
            
            if node == dst:
                return weight
            if k < 0:
                continue  # need to search target in the queue
            
            for adj in g[node].keys():
                if adj in visit:
                    continue
                heapq.heappush(q, (weight + g[node][adj], adj, k - 1))
        
        return -1





stime = time.time()
print(200 == Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, K=1))
print('elapse time: {} sec'.format(time.time() - stime))

