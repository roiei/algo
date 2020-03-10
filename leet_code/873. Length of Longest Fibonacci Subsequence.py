import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def lenLongestFibSubseq(self, A: [int]) -> int:

        most = max(A)
        dp = [1]*2
        i = 2
        while dp[-1] < most:
            dp.insert(i, dp[i-1] + dp[i-2])
            i += 1
        
        a = list(set(A))
        m = len(dp)
        n = len(a)
        i = j = 0
        cnt = 0

        print(a)
        print(dp)
        
        while i < m and j < n:
            
            if dp[i] == a[j]:
                cnt += 1
                i += 1
                j += 1
                continue
            if dp[i] > a[j]:
                j += 1
                continue
            if dp[i] < a[j]:
                i += 1
                continue
        return cnt
        
            

stime = time.time()
#print(5 == Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(3 == Solution().lenLongestFibSubseq([1,3,7,11,12,14,18]))
print('elapse time: {} sec'.format(time.time() - stime))