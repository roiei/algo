
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        n = len(A)
        l, r = 0, 0
        cnt = 0
        tot = 0
        
        for r in range(n):
            tot += A[r]
            
            while l < r and tot > S:
                tot -= A[l]
                l += 1
            
            if tot == S:
                cnt += 1
            
            i = l
            while tot == S and i < r and A[i] == 0:
                cnt += 1
                i += 1
        
        
        return cnt

            
stime = time.time()
print(Solution().numSubarraysWithSum(7))
print('elapse time: {} sec'.format(time.time() - stime))