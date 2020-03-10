
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_a = len(A)
        len_b = len(B)
        
        dp = [[0]*(len_a) for _ in range(len_b)]
        
        for i in range(len_a):
            for j in range(len_b):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
        
        return max(max(line) for line in dp)


stime = time.time()
print(4 == Solution().minSubArrayLen([1, -1, 5, -2, 3], 3))
print(2 == Solution().minSubArrayLen([-2, -1, 2, 1], 1))
print('elapse time: {} sec'.format(time.time() - stime))