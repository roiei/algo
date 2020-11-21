import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: [[int]], k: int) -> int:
        inbound = collections.defaultdict(int)
        outbound = collections.defaultdict(int)
        g = collections.defaultdict(list)

        for i in range(1, n + 1):
            inbound[i] = 0
            outbound[i] = 0

        for u, v in dependencies:
            g[u] += v,
            inbound[v] += 1
            outbound[u] += 1

        visited = set()
        sem = 0
        q = []

        while True:
            leftk = k

            for u, inb in inbound.items():
                if inb == 0 and u not in visited:
                    q += u,
                    visited.add(u)

            if not q:
                break

            with_outs = [u for u in q if outbound[u]]
            without_outs = [u for u in q if not outbound[u]]
            q = with_outs + without_outs

            while q and leftk:
                u = q.pop(0)

                for v in g[u]:
                    if v in visited:
                        continue

                    if inbound[v]:
                        inbound[v] -= 1

                leftk -= 1

            sem += 1

        return sem


stime = time.time()
print(3 == Solution().minNumberOfSemesters(n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2))
print(4 == Solution().minNumberOfSemesters(n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2))
print(6 == Solution().minNumberOfSemesters(n = 11, dependencies = [], k = 2))
print(3 == Solution().minNumberOfSemesters(8, [[1,6],[2,7],[8,7],[2,5],[3,4]], 3))
print(3 == Solution().minNumberOfSemesters(3, [[2,3],[2,1]], 1))
print(5 == Solution().minNumberOfSemesters(9, [[4,8],[3,6],[6,8],[7,6],[4,2],[4,1],[4,7],[3,7],[5,2],[5,9],[3,4],[6,9],[5,7]], 2))
print('elapse time: {} sec'.format(time.time() - stime))

