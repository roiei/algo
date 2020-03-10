
import time
from util_list import *
from util_tree import *
import copy
import collections



class Solution:
    def search(self, nums, val):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == val:
                s = e = m
                j = m-1
                while j >= 0:
                    if nums[j] == val:
                        s = j
                    j -= 1
                j = m+1
                while j <= len(nums)-1:
                    if nums[j] == val:
                        e = j
                    j += 1
                return [s, e]
            if nums[m] > val:
                r = m-1
            else:
                l = m+1
        return [-1, -1]

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        return self.search(nums, target)


stime = time.time()
print(Solution().searchRange([5,7,7,8,8,10], 8))
print('elapse time: {} sec'.format(time.time() - stime))