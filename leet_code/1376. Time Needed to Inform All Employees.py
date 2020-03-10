
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: [int], informTime: [int]) -> int:
        mn = len(manager)
        if n != mn:
            return -1

        g = collections.defaultdict(list)

        for i, par in enumerate(manager):
            g[par] += (i, informTime[i]),

        visited = {headID}
        mx = 0

        q = [(headID, informTime[headID])]
        while q:
            u, inc_cost = q.pop(0)
            mx = max(mx, inc_cost)

            for v, cost in g[u]:
                if v in visited:
                    continue

                visited.add(v)
                q += (v, inc_cost + cost),

        return mx
            
            
stime = time.time()
print(21 == Solution().numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))