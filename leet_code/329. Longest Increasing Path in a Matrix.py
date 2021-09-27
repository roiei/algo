import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for i in range(rows)]

        def dfs(y, x, prev):
            if matrix[y][x] <= prev:
                return 0
            if 0 == dp[y][x]:
                res = [0]
                for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if not (0 <= y+oy < rows and 0 <= x+ox < cols):
                        continue
                    res += dfs(y+oy, x+ox, matrix[y][x]),
                dp[y][x] = max(res)+1
            return dp[y][x]

        res = []
        for y in range(rows):
            for x in range(cols):
                res += dfs(y, x, matrix[y][x]-1),
        return max(res)

    def longestIncreasingPath(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(y, x, prev):
            if matrix[y][x] <= prev:
                return 0

            if (y, x) in mem:
                return mem[(y, x)]

            mx = 0
            for oy, ox in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny = y + oy
                nx = x + ox

                if not (0 <= ny < rows and 0 <= nx < cols):
                    continue

                mx = max(mx, dfs(ny, nx, matrix[y][x]))

            mem[(y, x)] = mx + 1
            return mem[(y, x)]

        mem = {}
        mx = 0
        for y in range(rows):
            for x in range(cols):
                mx = max(mx, dfs(y, x, matrix[y][x] - 1))
        return mx


print(4 == Solution().longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])) # 4 (1, 2, 6, 9)
print(4 == Solution().longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])) # 4
print(4 == Solution().longestIncreasingPath([[7,7,5],[2,4,6],[8,2,0]])) # 4
print(6 == Solution().longestIncreasingPath([[7,8,9],[9,7,6],[7,2,3]])) # 6, 2->3->6->7->8->9
