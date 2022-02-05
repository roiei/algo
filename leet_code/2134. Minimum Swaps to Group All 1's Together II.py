import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        zeros = nums[:ones].count(0)
        mn_zeros = zeros

        for i in range(n - 1):
            if nums[i] == 0:
                zeros -= 1

            if nums[(i + ones)%n] == 0:
                zeros += 1

            mn_zeros = min(mn_zeros, zeros)

        return mn_zeros


stime = time.time()
print(1 == Solution().minSwaps(nums = [0,1,0,1,1,0,0]))
print('elapse time: {} sec'.format(time.time() - stime))