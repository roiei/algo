import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return max((max(row) for row in dp))


    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                if text1[y - 1] == text2[x - 1]:
                    dp[y][x] = dp[y - 1][x - 1] + 1
                else:
                    dp[y][x] = max(dp[y - 1][x], dp[y][x - 1])
        
        return dp[-1][-1]



stime = time.time()
print(3 == Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))
print('elapse time: {} sec'.format(time.time() - stime))


