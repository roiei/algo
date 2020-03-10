
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maxValueAfterReverse(self, nums: [int]) -> int:
        A = nums
        total = 0
        res = 0
        min2 = float('inf')
        max2 = float('-inf')

        print(list(zip(A, A[1:])))
        
        for a, b in zip(A, A[1:]):
            total += abs(a - b)
            res = max(res, abs(A[0] - b) - abs(a - b))
            res = max(res, abs(A[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
            
        return total + max(res, (max2 - min2) * 2)

            
stime = time.time()
print(10 == Solution().maxValueAfterReverse(nums = [2,3,1,5,4]))
print(68 == Solution().maxValueAfterReverse(nums = [2,4,9,24,2,1,10]))
print('elapse time: {} sec'.format(time.time() - stime))