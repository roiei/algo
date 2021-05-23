import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > 6*len(nums2) or len(nums2) > 6*len(nums1):
            return -1
        
        diff = sum(nums1) - sum(nums2)
        if diff == 0:
            return 0

        if sum(nums1) < sum(nums2):
            nums1, nums2 = nums2, nums1
            diff = abs(diff)
        
        nums1.sort(key=lambda x:-x)
        nums2.sort()
        
        res = p1 = p2 = 0

        while diff > 0:
            res += 1
            n1 = nums1[p1] - 1 if p1 < len(nums1) else -1
            n2 = 6 - nums2[p2] if p2 < len(nums2) else -1
            if n1 > n2:
                diff -= n1
                p1 += 1
            else:
                diff -= n2
                p2 += 1

        return res

            

stime = time.time()
print(3 == Solution().minOperations(nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]))
print(-1 == Solution().minOperations(nums1 = [1,1,1,1,1,1,1], nums2 = [6]))
print('elapse time: {} sec'.format(time.time() - stime))