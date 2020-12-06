
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



class Solution:
    def search(self, nums, val):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r)//2
            if nums[m] == val:
                s = e = m
                j = m - 1
                while j >= 0:
                    if nums[j] == val:
                        s = j
                    j -= 1
                j = m + 1
                while j <= len(nums) - 1:
                    if nums[j] == val:
                        e = j
                    j += 1
                return [s, e]
            if nums[m] > val:
                r = m - 1
            else:
                l = m + 1

        return [-1, -1]

    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        return self.search(nums, target)

    def searchRange(self, nums, target):
        def _search(nums, target, left):
            l = 0
            r = len(nums)

            while l < r:
                m = (l + r)//2
                if nums[m] > target or (left and nums[m] == target):
                    r = m
                else:
                    l = m + 1

            return l

        l_idx = _search(nums, target, True)
        if l_idx == len(nums) or nums[l_idx] != target:
            return [-1, -1]

        return [l_idx, _search(nums, target, False) - 1]



stime = time.time()
print([3,4] == Solution().searchRange([5,7,7,8,8,10], 8))
print([-1, -1] == Solution().searchRange([5,7,7,8,8,10], 6))
print([-1, -1] == Solution().searchRange([], 0))
print('elapse time: {} sec'.format(time.time() - stime))