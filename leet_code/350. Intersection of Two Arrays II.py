import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        if not nums1 or not nums2:
            return []
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        if l1 > l2:
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        
        long.sort()
        short.sort()
        
        res = []
        i = j = 0
        
        for i, num in enumerate(long):
            if num in short:
                res += num,
                short.pop(short.index(num))
        
        return res


stime = time.time()

print([2,2] == Solution().intersect([1,2,2,1], [2,0,2]))
print('elapse time: {} sec'.format(time.time() - stime))