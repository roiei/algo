
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        l = 1
        r = len(A) - 1
        
        left = A[:1]
        right = sorted(A[1:])
        
        mx = left[-1]
        mn = right[0]
        
        while l < r:
            if mx <= mn:
                break
            
            idx = bisect.bisect_left(right, A[l])
            right.pop(idx)

            idx = bisect.bisect_left(left, A[l])
            left.insert(idx, A[l])
            
            mx = left[-1]
            mn = right[0]

            l += 1
        
        return l
    
    def partitionDisjoint(self, A):
        n = len(A)
        left_mxs = [0]*n
        right_mns = [0]*n

        mx = float('-inf')
        for i in range(n):
            mx = max(mx, A[i])
            left_mxs[i] = mx

        mn = float('inf')
        for i in range(n - 1, -1, -1):
            mn = min(mn, A[i])
            right_mns[i] = mn

        for i in range(1, n):
            if left_mxs[i - 1] <= right_mns[i]:
                return i


stime = time.time()
print(3 == Solution().convert([5,0,3,8,6]))  # left = [5,0,3], right = [8,6]
print(4 == Solution().convert([1,1,1,0,6,12]))  # left = [1,1,1,0], right = [6,12]
print('elapse time: {} sec'.format(time.time() - stime))