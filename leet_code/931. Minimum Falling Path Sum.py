import time
from util_list import *


class Solution:
    def minFallingPathSum(self, A: 'List[List[int]]') -> int:
        if not A:
            return -1
        rows = len(A)
        cols = len(A[0])
        if 1 == rows:
            if 1 == cols:
                return A[0][0]
            return min(A[0])
        for y in range(1, rows):
            for x in range(cols):
                if 0 == x:
                    A[y][x] += min(A[y-1][x], A[y-1][x+1])
                elif cols-1 == x:
                    A[y][x] += min(A[y-1][x-1], A[y-1][x])
                else:
                    A[y][x] += min(A[y-1][x-1], A[y-1][x], A[y-1][x+1])
        return min(A[-1])


stime = time.time()
print(12 == Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(69 == Solution().minFallingPathSum([[69]]))
print('elapse time: {} sec'.format(time.time() - stime))
