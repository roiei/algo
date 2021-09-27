import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stk = []
        right_bigger = collections.defaultdict(int)
        
        for i, num in enumerate(nums2):
            while stk and stk[-1] < num:
                val = stk.pop()
                right_bigger[val] = num
            
            stk += num,
        
        while stk:
            val = stk.pop()
            right_bigger[val] = -1
        
        res = []
        for num in nums1:
            res += right_bigger[num],
        
        return res


stime = time.time()
print([-1,3,-1] == Solution().nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print('elapse time: {} sec'.format(time.time() - stime))
