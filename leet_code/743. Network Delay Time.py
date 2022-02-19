import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w

        visit = [False]*(N+1)
        q = [(0, K)]
        num_nodes = N
        weight = 0
        mweight = 0

        while q:
            weight, u = heapq.heappop(q)
            if visit[u] == True:
                continue
                
            mweight = weight
            visit[u] = True
            num_nodes -= 1

            for v, w in graph[u].items():
                if visit[v] == False:
                    heapq.heappush(q, (weight + w, v))

        if num_nodes > 0:
            return -1

        return -1 if mweight == 0 else mweight

    def get_min_delay(self, links: List[List[int]], n: int, start_node: int) -> int:
        g = collections.defaultdict(dict)
        for u, v, w in links:
            g[u][v] = w
        
        q = [(0, start_node)]
        visited = set()
        mn = 0
        
        while q:
            inc, u = heapq.heappop(q)
            visited.add(u)

            if len(visited) == n:
                return inc
            
            for v, w in g[u].items():
                if v in visited:
                    continue
                
                heapq.heappush(q, (inc + w, v))
        
        return -1

    def get_min_delay(self, links: List[List[int]], n: int, start_node: int) -> int:
        dists = collections.defaultdict(lambda: float('inf'))
        g = collections.defaultdict(dict)
        for u, v, w in links:
            g[u][v] = w
        
        q = [(0, start_node)]
        dists[start_node] = 0
        mn = 0
        visited = set()
        
        while q:
            inc, u = heapq.heappop(q)
            visited.add(u)
            
            if len(visited) == n:
                return max(dists.values())

            if dists[u] < inc:
                continue

            for v, w in g[u].items():
                if v in visited:
                    continue
                    
                if dists[v] < w + inc:
                    continue
                dists[v] = w + inc
                heapq.heappush(q, (inc + w, v))
        
        return max(dists.values()) if len(visited) == n else -1


stime = time.time()
print(8 == Solution().get_min_delay([[1,2,3],[1,3,5],[2,3,2],[2,4,1],[4,3,3],[3,5,3],[4,5,8]], 5, 1))
#print(2 == Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1))
#print(-1 == Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))
print('elapse time: {} sec'.format(time.time() - stime))

#z = (a+b) * (c+d)



