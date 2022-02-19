
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n + 1) for i in range(n + 1)]        
        rs = s[::-1]
        
        for i in range(n):
            for j in range(n):
                if s[i] == rs[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return n - dp[-1][-1]

    def find_min_num_letters(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n + 1) for i in range(n + 1)]        
        rs = s[::-1]
        
        for i in range(n):
            for j in range(n):
                if s[i] == rs[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        
        return n - dp[-1][-1]



stime = time.time()
#print(0 == Solution().minInsertions("zzazz"))
#print(5 == Solution().minInsertions("leetcode"))
#print(5 == Solution().minInsertions("zjveiiwvc"))
print(Solution().minInsertions("ziveii"))
01: n = find_min_num_letters("ziveii")
02: print(n)
print('elapse time: {} sec'.format(time.time() - stime))