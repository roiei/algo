
import time
from util.util_list import *
from util.util_tree import *
import copy
import bisect
import collections


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if not A:
            return False
        
        mx = max(A)
        idx = A.index(mx)
        
        if idx == 0 or idx == len(A) - 1:
            return False
        
        pre = A[idx]
        for i in range(idx - 1, -1, -1):
            if not A[i] < pre:
                return False
            pre = A[i]
        
        pre = A[idx]
        for i in range(idx + 1, len(A)):
            if not pre > A[i]:
                return False
            pre = A[i]
        
        return True
        

stime = time.time()
print(False == Solution().validMountainArray([2,1]))
print(False == Solution().validMountainArray([3,5,5]))
print(True == Solution().validMountainArray([0,3,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))