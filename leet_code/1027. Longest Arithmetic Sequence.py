import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq


class Solution(object):
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = [[-1]*n for _ in range(n)]
        freq = collections.defaultdict(list)
        mx = 0
        
        for y in range(n - 1):
            for x in range(y + 1, n):
                diff = A[y] - A[x]
                pre = freq[diff]
                
                if not pre:
                    freq[diff] = [A[y], A[x]]
                elif pre[-1] != A[y]:
                    freq[diff] = [A[y], A[x]]
                else:
                    freq[diff] += A[x],
                
                mx = max(mx, len(freq[diff]))
        
        return mx
    
    
    def longestArithSeqLength(self, A):
        n = len(A)
        dp = [{} for _ in range(n)]
        mx = 0
        
        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                mx = max(mx, dp[i][diff])
                
        return mx
                       


stime = time.time()
print(6 == Solution().findBlackPixel([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]))
print('elapse time: {} sec'.format(time.time() - stime))
