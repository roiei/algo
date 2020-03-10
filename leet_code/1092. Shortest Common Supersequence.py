import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):

        m = len(str1)
        n = len(str2)
        
        dp = [list(range(n + 1))]
        dp += [[i] + [0]*n for i in range(1, m + 1)]

        
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j + 1])

        for line in dp:
            print(line)
                
        i = m
        j = n
        scs = ''
        
        while i*j:
            f1 = str1[i - 1] == str2[j - 1]
            f2 = dp[i - 1][j] < dp[i][j - 1]

            unit1 = int(f1 or f2)
            unit2 = int(f1 or not f2)

            scs = str1[i - 1]*unit1 + str2[j - 1]*(1 - unit1) + scs

            print(scs)

            i -= unit1
            j -= unit2

        return str1[:i] + str2[:j] + scs


stime = time.time()
print("cabac" == Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
print('elapse time: {} sec'.format(time.time() - stime))


