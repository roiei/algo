import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


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


stime = time.time()
print(2 == Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1))
print(-1 == Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2))
print('elapse time: {} sec'.format(time.time() - stime))

