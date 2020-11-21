import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def numSubmat(self, mat: [[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        dp = [[[0, 0, 0] for x in range(cols)] for y in range(rows)]
        cnt = 0

        for y in range(rows):
            for x in range(cols):
                # for d in dp:
                #     print(d)
                if y - 1 >= 0 and mat[y - 1][x] == 1:
                    dp[y][x][0] = dp[y - 1][x][0] + 1
                else:
                    dp[y][x][0] = 0
                
                if x - 1 >= 0 and mat[y][x - 1] == 1:
                    dp[y][x][1] = dp[y][x - 1][1] + 1
                else:
                    dp[y][x][1] = 0
                
                if (y - 1 >= 0 and mat[y - 1][x] == 1 and
                    x - 1 >= 0 and mat[y][x - 1] == 1 and
                    mat[y - 1][x - 1] == 1):
                    dp[y][x][2] = dp[y - 1][x - 1][2] + 1
                else:
                    dp[y][x][2] = 0
            
                if mat[y][x] == 0:
                    continue

                # for d in dp:
                #     print(d)

                cnt += 1
                cnt += dp[y][x][0]
                cnt += dp[y][x][1]
                cnt += dp[y][x][2]

                print(f'y = {y}, x = {x}, inc = {1 + dp[y][x][0] + dp[y][x][1] + dp[y][x][2]}')
        
        print(cnt)
        return cnt


    def numSubmat(self, mat: [[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])

        res = 0
        dp = [0]*cols

        for y in range(rows):
            for x in range(cols):
                dp[x] = 0 if mat[y][x] == 0 else dp[x] + 1
                mn = dp[x]

                print(f'y = {y}, x = {x}')

                for i in range(x, -1, -1):
                    mn = min(mn, dp[i])
                    print(f' + {mn}')
                    res += mn

        return res




stime = time.time()
print(13 == Solution().numSubmat(mat = [[1,0,1], [1,1,0],[1,1,0]]))
# print(7 == Solution().numSubmat([[0,1],[1,1],[1,0]]))
# print(24 == Solution().numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]))
print('elapse time: {} sec'.format(time.time() - stime))

