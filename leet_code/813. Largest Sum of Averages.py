
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def largestSumOfAverages(self, A: [int], K: int) -> float:
        
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        print(P)
            
        def average(i, j):
            return (P[j] - P[i]) / float(j - i)

        n = len(A)
        dp = [average(i, n) for i in range(n)]

        print(dp)
        
        for k in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], average(i, j) + dp[j])

        return dp[0]
    

stime = time.time()
#print(20 == Solution().largestSumOfAverages([9,1,2,3,9], 3))
print(20.5 == Solution().largestSumOfAverages([1,2,3,4,5,6,7], 4))
#print(1 == Solution().maximizeSweetness([5,6,7,8,9,1,2,3,4], K = 8))
print('elapse time: {} sec'.format(time.time() - stime))