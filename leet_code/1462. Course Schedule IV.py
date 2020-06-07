
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: [[int]], queries: [[int]]) -> [bool]:
        res = []
        g = collections.defaultdict(list)
        for u, v in prerequisites:
            g[u] += v,

        for u, target in queries:
            q = [u]
            visited = set()
            visited.add(u)
            valid = False

            while q:
                u = q.pop(0)
                if u == target:
                    valid = True
                    break

                for v in g[u]:
                    if v in visited:
                        continue

                    visited.add(v)
                    q += v,

            res += valid,

        return res


stime = time.time()
print([False,True] == Solution().checkIfPrerequisite(n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
print([False,False] == Solution().checkIfPrerequisite(n = 2, prerequisites = [], queries = [[1,0],[0,1]]))
print('elapse time: {} sec'.format(time.time() - stime))

