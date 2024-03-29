
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if not A:
            return False
        if n == 1:
            return True
        inc = True

        pre = A[0]
        start = 0
        for i in range(1, n):
            if pre == A[i]:
                start += 1
            elif pre < A[i]:
                break
            elif pre > A[i]:
                inc = False
                break
            pre = A[i]

        if inc == False:
            for i in range(start, n):
                if 0 > pre - A[i]:
                    return False
                pre = A[i]
        else:
            for i in range(start, n):
                if 0 > A[i] - pre:
                    return False
                pre = A[i]
        return True

    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums:
            return False

        if nums[0] > nums[-1]:
            nums = nums[::-1]

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False

        return True


stime = time.time()
print(True == Solution().isMonotonic([1,2,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))