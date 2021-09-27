import time
from util.util_list import *


class Solution:
    def check(self, N, depth, m, n, i, j):
        if (i,j,depth) in self.mem:
            return self.mem[(i,j,depth)]
        if 0 > i or i > m-1 or 0 > j or j > n-1:
            return 1
        if N == depth:
           return 0
        res = [0]
        for offy, offx in self.dirs:
            res.append(self.check(N, depth+1, m, n, i+offy, j+offx))
        self.mem[(i,j,depth)] = sum(res)
        return sum(res)

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        if 0 == N:
            return 0
        self.mem = {}
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ret = self.check(N, 0, m, n, i, j)
        return ret % (10 ** 9 + 7)

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def dfs(y, x, move):
            if (y, x, move) in mem:
                return mem[(y, x, move)]

            if move == 0:
                return 0

            cnt = 0
            for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = oy + y, ox + x
                if not (0 <= ny < m and 0 <= nx < n):
                    cnt += 1
                    continue
                
                cnt += dfs(ny, nx, move - 1)

            mem[(y, x, move)] = cnt
            return cnt

        mem = {}
        ret = dfs(i, j, N)
        return ret%(10**9 + 7)


stime = time.time()
#print(6 == Solution().findPaths(2, 2, 2, 0, 0))
print(914783380 == Solution().findPaths(8,50,23,5,26))
print('elapse time: {} sec'.format(time.time() - stime))
