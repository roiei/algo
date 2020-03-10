
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def countComponents(self, n, edges) -> int:
        g = collections.defaultdict(dict)
        visited = set()
        cnt = 0

        for u, v in edges:
            g[u][v] = True
            g[v][u] = True

        for i in range(n):
            if i in visited:
                continue

            q = [i]
            visited.add(i)

            while q:
                u = q.pop(0)

                for v, linked in g[u].items():
                    if v in visited:
                        continue

                    visited.add(v)
                    q += v,

            cnt += 1

        return cnt



stime = time.time()
print(2 == Solution().countComponents(n = 5, edges = [[0, 1], [1, 2], [3, 4]]))
print('elapse time: {} sec'.format(time.time() - stime))