
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List
import bisect


class Solution:
    def partitionDisjoint(self, A):
        if not A:
            return 0

        left = [A.pop(0)]
        right = sorted(A)

        for i in range(len(A)):
            if left[-1] <= right[0]:
                break

            idx = bisect.bisect_left(left, A[i])
            left.insert(idx, A[i])

            idx = bisect.bisect_left(right, A[i])
            right.pop(idx)

        return len(left)
    
    def partitionDisjoint(self, A):
        n = len(A)
        left_mxs = [float('-inf')]*n
        right_mns = [float('inf')]*n

        mx = float('-inf')
        mn = float('inf')
        
        for i in range(n):
            mx = max(mx, A[i])
            left_mxs[i] = mx

            mn = min(mn, A[n - 1 - i])
            right_mns[n - 1 - i] = mn

        for i in range(1, n):
            if left_mxs[i - 1] <= right_mns[i]:
                return i

    def partitionDisjoint(self, nums: List[int]) -> int:
        mns = []
        mn = float('inf')
        
        for i in range(len(nums) - 1, -1, -1):
            mn = min(mn, nums[i])
            mns.insert(0, mn)
        
        mx = nums[0]
        for i in range(1, len(nums)):
            if mx <= mns[i]:
                return i
            mx = max(mx, nums[i])
        
        return i


stime = time.time()
print(3 == Solution().partitionDisjoint([5,0,3,8,6]))  # left = [5,0,3], right = [8,6]
print(4 == Solution().partitionDisjoint([1,1,1,0,6,12]))  # left = [1,1,1,0], right = [6,12]
print('elapse time: {} sec'.format(time.time() - stime))