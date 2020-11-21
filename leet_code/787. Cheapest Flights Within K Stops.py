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

    def findCheapestPrice(self, n, flights, src, dst, K):
        g = collections.defaultdict(dict)
        for u, v, w in flights:
            g[u][v] = w
        
        q = [(0, src, K)]
        visited = set()
        
        while q:
            w, u, k = heapq.heappop(q)
            visited.add(u)
            
            if u == dst:
                return w
            
            if k < 0:
                continue
            
            for v, weight in g[u].items():
                if v in visited:
                    continue
                
                heapq.heappush(q, (w + weight, v, k - 1))
        
        return -1

    def findCheapestPrice(self, n, flights, src, dst, K):
        g = collections.defaultdict(dict)
        for u, v, w in flights:
            g[u][v] = w
        
        q = [(0, src, K + 1)]
        
        while q:
            tot_cost, u, k = heapq.heappop(q)

            if u == dst:
                print(tot_cost)
                return tot_cost
            
            if k == 0:
                continue
            
            for v, cost in g[u].items():
                heapq.heappush(q, (tot_cost + cost, v, k - 1))
        
        return -1



stime = time.time()

print(11 == Solution().findCheapestPrice(11, [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]], 0, 2, 4))
print(7 == Solution().findCheapestPrice(5, [[0,1,1],[0,2,5],[1,2,1],[2,3,1],[3,4,1]], 0, 4, 2))
print(200 == Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, K=1))
print('elapse time: {} sec'.format(time.time() - stime))

