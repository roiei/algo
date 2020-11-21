import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        if len(nums1) > len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        
        res = []

        for i, num in enumerate(short):
            if num in long:
                res += long.pop(long.index(num)),
        
        return res


stime = time.time()
print([1,2] == Solution().intersect([2,1], [1, 2]))
#print([2,2] == Solution().intersect([1,2,2,1], [2,0,2]))
print('elapse time: {} sec'.format(time.time() - stime))