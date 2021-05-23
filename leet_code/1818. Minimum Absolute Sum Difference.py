
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


# You are given two positive integer arrays nums1 and nums2, both of length n.

# The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

# You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

# Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:


stime = time.time()
print(3 == Solution().minAbsoluteSumDiff(nums1 = [1,7,5], nums2 = [2,3,5]))
print('elapse time: {} sec'.format(time.time() - stime))