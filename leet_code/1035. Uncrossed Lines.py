
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
        return dp[-1][-1]
                    


stime = time.time()
print(2 == Solution().maxUncrossedLines(A = [1,4,2], B = [1,2,4]))
print(3 == Solution().maxUncrossedLines(A = [2,5,1,2,5], B = [10,5,2,1,5,2]))
print(2 == Solution().maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]))
print('elapse time: {} sec'.format(time.time() - stime))