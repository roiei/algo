import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = len(nums1)
        n = len(nums2)

        if m > n:
            shorter, slen = nums2, n
            longer, llen = nums1, m
        else:
            shorter, slen = nums1, m
            longer, llen = nums2, n

        res = set()
        for num in shorter:
            if num not in longer:
                continue

            res.add(longer.pop(longer.index(num)))

        return list(res)


stime = time.time()
print([2] == Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2]))
print('elapse time: {} sec'.format(time.time() - stime))
