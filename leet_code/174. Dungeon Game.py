import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def calculateMinimumHP(self, dungeon: [[int]]) -> int:
        if not dungeon:
            return 
        r, c = len(dungeon), len(dungeon[0])
        
        dp = [[0 for _ in range(c)] for _ in range(r)]
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        for i in range(c-2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1] - dungeon[-1][i])
            
        for i in range(r-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])

        for l in dp:
            print(l)
            
        for i in range(r - 2, -1, -1):
            for j in range(c - 2, -1, -1):
                mn = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, mn - dungeon[i][j])
                
        for l in dp:
            print(l)
        return dp[0][0]


stime = time.time()
print(7 == Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
print('elapse time: {} sec'.format(time.time() - stime))