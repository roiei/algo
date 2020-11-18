import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


"""

8  9   2   7   8  6
0  1  -7  -5  -1  2

8  9   2   7   8  6
      ---
stk = 8 9 2
len = 3

transfer to new stak the less values than me '7'
transfer to new stak the less values than me '2'

stk = 2
8  9   2   7   8  6
      ---

8  9   2   7   8  6
                 ---

stk = 2 7 8 6
len = 4
"""


class Solution:
    def longestMountain(self, A: [int]) -> int:
        i = 0
        n = len(A)
        mx = 0
        stk = []
        
        while i < n:
            cur = A[i]

            while stk and stk[-1] < cur:
                cur = stk[-1]
                stk.pop(),
                i -= 1

            stk = []
            pre = i
            while i + 1 < n and A[i] < A[i + 1]:
                stk += A[i],
                i += 1

            if pre == i:
                i += 1
                continue

            pre = i
            while i + 1 < n and A[i] > A[i + 1]:
                stk += A[i],
                i += 1

            if pre == i:
                i += 1
                continue

            stk += A[i],
            mx = max(mx, len(stk))
            i += 1

        return mx


stime = time.time()
print(5 == Solution().longestMountain([2,1,4,7,3,2,5]))
print(0 == Solution().longestMountain([2,2,2]))
print(0 == Solution().longestMountain([2,3]))
print(4 == Solution().longestMountain([875,884,239,731,723,685]))
print('elapse time: {} sec'.format(time.time() - stime))