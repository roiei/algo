
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def maxSideLength(self, mat: [[int]], threshold: int) -> int:
        
        rows = len(mat)
        cols = len(mat[0])
        
        n = min(rows, cols)
        dp = [[0]*n for _ in range(n)]
        
        for y in range(n):
            for x in range(n):
                if x == 0:
                    dp[y][x] = mat[y][x]
                else:
                    dp[y][x] = mat[y][x] + dp[y][x - 1]
        
        for x in range(n):
            for y in range(1, n):
                dp[y][x] += dp[y - 1][x]

        for i in range(rows):
            print(dp[i])
        
        mx = 0
        for i in range(n):
            if dp[i][i] <= threshold:
                mx = dp[i][i]
        
        return mx**0.5


stime = time.time()
print(2 == Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4))
print('elapse time: {} sec'.format(time.time() - stime))