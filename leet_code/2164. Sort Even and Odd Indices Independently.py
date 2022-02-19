
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []
        for i, num in enumerate(nums):
            if i % 2:
                odds += num,
            else:
                evens += num,

        odds.sort(reverse=True)
        evens.sort()

        j = 0
        k = 0
        for i, num in enumerate(nums):
            if i % 2:
                nums[i] = odds[j]
                j += 1
            else:
                nums[i] = evens[k]
                k += 1

        return nums


stime = time.time()
print([2,3,4,1] == Solution().sortEvenOdd(nums=[4,1,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))