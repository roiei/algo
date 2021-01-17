import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


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

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        i = j = 0
        if len(nums1) > len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1

        res = []
        
        while i < len(long) and j < len(short):
            print(long[i], short[j])
            if long[i] == short[j]:
                res += long[i],
                j += 1
            i += 1
        

        return res


stime = time.time()
#print([1,2] == Solution().intersect([2,1], [1, 2]))
print([4,9] == Solution().intersect([4,9,5], [9,4,9,8,4]))
print([1] == Solution().intersect([2,1], [1,1]))
#print([2,2] == Solution().intersect([1,2,2,1], [2,0,2]))
print('elapse time: {} sec'.format(time.time() - stime))