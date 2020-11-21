import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from functools import lru_cache


class Solution:
    def maxProductPath(self, grid: [[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # not possible to use memorization with (y, x, tot)
        # cuz different route can be created on the path.
        
        def dfs(y, x, tot):
            tot *= grid[y][x]

            if y == rows - 1 and x == cols - 1:
                return tot

            res = []
            if y + 1 < rows:
                res += dfs(y + 1, x, tot),

            if x + 1 < cols:
                res += dfs(y, x + 1, tot),

            return max(res) if res else -1
        
        ret = dfs(0, 0, 1)
        if ret == -1:
            return -1

        return ret%(10**9 + 7)

    def maxProductPath(self, g: [[int]]) -> int:
        mod = 10**9 + 7
        M, N = len(g), len(g[0])
        dp = [[(float('-inf'), float('inf'))]*N for _ in range(M)]
        dp[0][0] = (g[0][0], g[0][0])
        for i in range(M):
            for j in range(N):
                if i==0 and j==0: continue
                cur = g[i][j]
                if cur == 0:
                    dp[i][j] = 0, 0
                    continue
                mx1, mn1 = dp[i-1][j] if i else (float('-inf'), float('inf'))
                mx2, mn2 = dp[i][j-1] if j else (float('-inf'), float('inf'))
                mx, mn = max(mx1, mx2)*cur, min(mn1, mn2)*cur
                dp[i][j] = (mx, mn) if cur>0 else (mn, mx)
        return dp[-1][-1][0] % mod if dp[-1][-1][0]>=0 else -1


stime = time.time()
#print(3 == Solution().maxProductPath([[3]]))
#print(Solution().maxProductPath([[4,3]]))
# print(0 == Solution().maxProductPath([
#     [1,3],
#     [0,-4]]))
# print(-1 == Solution().maxProductPath([
#     [-1,-2,-3],
#     [-2,-3,-3],
#     [-3,-3,-2]]))
print(19215865 == Solution().maxProductPath([[2,1,3,0,-3,3,-4,4,0,-4],[-4,-3,2,2,3,-3,1,-1,1,-2],[-2,0,-4,2,4,-3,-4,-1,3,4],[-1,0,1,0,-3,3,-2,-3,1,0],[0,-1,-2,0,-3,-4,0,3,-2,-2],[-4,-2,0,-1,0,-3,0,4,0,-3],[-3,-4,2,1,0,-4,2,-4,-1,-3],[3,-2,0,-4,1,0,1,-3,-1,-1],[3,-4,0,2,0,-2,2,-4,-2,4],[0,4,0,-3,-4,3,3,-1,-2,-2]]))

print('elapse time: {} sec'.format(time.time() - stime))


# "  this   is  a sentence "

# 9/4 -> floating...
# 9/3 -> 3

# Input: text = "  walks  udp package   into  bar a"  11/5 = 2
# Output: "walks  udp  package  into  bar  a "