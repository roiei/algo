
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def minReorder(self, n: int, connections: [[int]]) -> int:
        g = collections.defaultdict(list)
        ori_g = collections.defaultdict(list)

        for u, v in connections:
            g[u] += v,
            g[v] += u,
            ori_g[u] += v,

        q = [0]
        visited = set()
        cnt = 0
        visited.add(0)

        while q:
            u = q.pop(0)

            for v in g[u]:
                if v in visited:
                    continue

                if u not in ori_g[v]:
                    cnt += 1
                visited.add(v)
                q += v,

        return cnt


stime = time.time()
print(3 == Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(0 == Solution().minReorder(3, [[1,0],[2,0]]))
print('elapse time: {} sec'.format(time.time() - stime))

