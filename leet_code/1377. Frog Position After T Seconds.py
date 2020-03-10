
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def frogPosition(self, n: int, edges: [[int]], t: int, target: int) -> float:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u] += v,
            #g[v] += u,

        visited = {1}
        q = [(1, 1, t)]

        while q and t:
            u, prob, left_sec = q.pop(0)
            n = len(g[u])

            if u == target:
                return prob

            for v in g[u]:
                if v in visited:
                    continue

                visited.add(v)
                q += (v, prob*(1/n), left_sec - 1),

        return u == target

    def frogPosition(self, n: int, edges: [[int]], t: int, target: int) -> float:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u] += v,
            g[v] += u,

        q = [(1, 0, 1.0)] # (start, time, prob)
        visited = {1}
            
        while q:
            u, time, inc_prob = q.pop(0)
            not_visited = len([1 for v in g[u] if v not in visited])
            
            if u == target:
                return inc_prob if time == t or (time < t and not_visited == 0) else 0
                    
            prob = 1/not_visited if not_visited else 0 
            
            for v in g[u]:
                if v in visited:
                    continue

                visited.add(v)
                q += (v, time + 1, inc_prob*prob),

        return 0

    def frogPosition2(self, n, edges, t, target):
        if n == 1:
            return 1.0

        g = collections.defaultdict(list)
        for u, v in edges:
            g[u] += v,
            g[v] += u,
        visited = {1}

        def dfs(u, t):
            n = len(g[u])
            if u != 1 and n == 1 or t == 0:
                return u == target

            visited.add(u)

            res = 0
            for v in g[u]:
                if v in visited:
                    continue
                res += dfs(v, t - 1)

            divisor = n
            if u != 1:
                divisor -= 1

            return res * 1.0 / divisor

        return dfs(1, t)


            
stime = time.time()
print(0.16666666666666666  == Solution().frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4))
print(0.16666666666666666  == Solution().frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 20, 6))
print(1.0  == Solution().frogPosition(3, [[2,1],[3,2]], 1, 2))
print(0.0  == Solution().frogPosition(8, [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]], 7, 7))
print('elapse time: {} sec'.format(time.time() - stime))