import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def jump(self, n, k, depth, r, c):
        if r < 0 or r > n-1 or c < 0 or c > n-1:
            return 0
        if k == depth:
            return 1
        if (r,c,depth) in self.mem:
            return self.mem[(r,c,depth)]
        prob = 1/8
        sprob = 0
        for offr, offc in self.dirs:
            sprob += prob*self.jump(n, k, depth+1, r+offr, c+offc)
        self.mem[(r,c,depth)] = sprob
        return sprob

    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if 0 == K and N >= 1:
            return 1
        if 2 >= N:
            return 0
        self.mem = {}
        self.dirs = [(1,2), (2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        ret = self.jump(N, K, 0, r, c)
        return ret

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if 0 == k and n >= 1:
            return 1

        def dfs(k, r, c):
            if (r, c, k) in mem:
                return mem[(r, c, k)]

            if k == 0:
                return 1

            cnt = 0
            for oy, ox in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
                ny, nx = oy + r, ox + c
                if not (0 <= ny < n and 0 <= nx < n):
                    continue

                cnt += dfs(k - 1, ny, nx)

            res = (1/8)*cnt
            mem[(r, c, k)] = res
            return res

        mem = {}
        ret = dfs(k, row, column)
        return ret


stime = time.time()
print(0.0625 == Solution().knightProbability(3, 2, 0, 0))
print(1 == Solution().knightProbability(1, 0, 0, 0))
print(0.0001905256629833365 == Solution().knightProbability(8, 30, 6, 4))
print('elapse time: {} sec'.format(time.time() - stime))
