import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = collections.defaultdict(list)

        for u, v in edges:
            g[u] += v,
            g[v] += u,

        q = [(0, 1)] # elapse time, node numger
        arrive = 0
        elapse_time = -1
        visited = collections.defaultdict(int)

        while q:
            elapse_time, u = q.pop(0)
            visited[u] += 1

            if u == n:
                arrive += 1

            if 2 == arrive:
                break

            turn = elapse_time//change
            left = elapse_time%change

            if turn%2:
                elapse_time += change - left

            for v in g[u]:
                if visited[v] == 2:
                    continue
                q += (elapse_time + time, v),

        return elapse_time

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = defaultdict(list)
        for (u,v) in edges:
            adj[u].append(v)
            adj[v].append(u)

        time_cache = [[float('inf'), float('inf')] for _ in range(n)]
        count = [0]*n
        K = 2
        pq = [(0, 1)]
        
        while(pq):
            t, node = heappop(pq)
            q, r = divmod(t, change)
            if(t >= time_cache[node-1][1] or t == time_cache[node-1][0]):
                continue
            if(t < time_cache[node-1][0]):
                time_cache[node-1][0], time_cache[node-1][1] = t, time_cache[node-1][0]
            elif(time_cache[node-1][0] < t < time_cache[node-1][1]):
                time_cache[node-1][1] = t
            count[node-1] += 1
            if(node == n and count[node-1] == K):
                return time_cache[node-1][1]
            for nxt in adj[node]:
                if(count[nxt-1] < K):
                    nv = t+change-r+time if(q%2) else t+time
                    heappush(pq, (nv, nxt))
        return -1


stime = time.time()
print(13 == Solution().secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
print(11 == Solution().secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2))
print('elapse time: {} sec'.format(time.time() - stime))