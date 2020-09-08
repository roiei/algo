import time
from util.util_list import *
from util.util_tree import *
import copy
import functools
import collections



class Solution:
    def largestComponentSize(self, A: [int]) -> int:
        g = collections.defaultdict(list)
        n = len(A)
        print(A)
        A.sort()
        print(A)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if A[j] - A[i] <= 1:
                    continue

                g[A[i]] += A[j],
                g[A[j]] += A[i],

        visited = set()
        mx = 0

        print(g)

        for node in A:
            q = [node]
            cnt = 1

            while q:
                u = q.pop(0)

                for v in g[u]:
                    if v in visited:
                        continue

                    visited.add(v)
                    q += v,
                    cnt += 1

            mx = max(mx, cnt)

        print(mx)
        return mx


stime = time.time()
print(8 == Solution().largestComponentSize([2,3,6,7,4,12,21,39]))
print('elapse time: {} sec'.format(time.time() - stime))