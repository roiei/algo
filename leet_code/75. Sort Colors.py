import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


stime = time.time()
print([0,0,1,1,2,2] == Solution().sortColors([2,0,2,1,1,0]))
print('elapse time: {} sec'.format(time.time() - stime))
