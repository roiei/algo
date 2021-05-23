import time
import re
import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for u, v in adjacentPairs:
            indegree[u] += 1
            indegree[v] += 1
            g[u] += v,
            g[v] += u,

        starts = [u for u, degree in indegree.items() if degree == 1]

        q = [starts[0]]
        visited = {starts[0]}
        trace = []

        while q:
            u = q.pop(0)
            trace += u,

            for v in g[u]:
                if v in visited:
                    continue

                visited.add(v)
                q += v,

        return trace


stime = time.time()
print([1,2,3,4] == Solution().restoreArray([[2,1],[3,4],[3,2]]))
print([-2,4,1,-3] == Solution().restoreArray([[4,-2],[1,4],[-3,1]]))
print([100000,-100000] == Solution().restoreArray([[100000,-100000]]))
print([7,2,-9,-3,6,1,-5,3,5,8] == Solution().restoreArray([[-3,-9],[-5,3],[2,-9],[6,-3],[6,1],[5,3],[8,5],[-5,1],[7,2]]))
print('elapse time: {} sec'.format(time.time() - stime))
