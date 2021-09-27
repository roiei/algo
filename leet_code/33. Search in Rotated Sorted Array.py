
import math
import heapq
import time
from typing import List


class Solution:
    def find_rot_ptr(self, nums, l, r):
        if l == r:
            return -1
        m = (l+r)//2
        if 0 < m:
            if nums[m-1] > nums[m]:
                return m-1 # rotation point
        if nums[m] > nums[m+1]:
            return m       # rotation point

        idx1 = -1
        if l <= m-1:
            idx1 = self.find_rot_ptr(nums, l, m-1)
        idx2 = self.find_rot_ptr(nums, m+1, r)

        if idx1 == -1 and idx2 == -1:
            return -1
        ret = idx2 if idx1 == -1 else idx1
        return ret

    def binary_search(self, nums, n, target):
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m+1
            if nums[m] > target:
                r = m-1
        return -1

    def search(self, nums: 'List[int]', target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        idx = self.find_rot_ptr(nums, 0, n-1)
        if -1 != idx and nums[idx] == target: # code below ignores pivot
            return idx
        res = -1
        if -1 != idx:
            left = nums[:idx]
            nleft = len(left)
            r1 = self.binary_search(left, nleft, target)
            right = nums[idx+1:]
            nright = len(right)
            r2 = self.binary_search(right, nright, target)
            if r1 != -1:
                res = r1
            elif r2 != -1:
                res = r2 + nleft + 1
        else:
            res = self.binary_search(nums, n, target)
        return res

    def search(self, nums: List[int], target: int) -> int:
        def bisearch(nums, target):
            l = 0
            r = len(nums) - 1

            while l <= r:
                m = (l + r)//2
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
            return -1

        def find_pivot(nums, l, r):
            if l > r:
                return -1

            m = (l + r)//2
            if m > 0 and nums[m - 1] > nums[m]:
                return m - 1

            if m + 1 <= r and nums[m] > nums[m + 1]:
                return m

            lidx = find_pivot(nums, l, m - 1)
            ridx = find_pivot(nums, m + 1, r)
            if -1 != lidx:
                return lidx
            if -1 != ridx:
                return ridx
            return -1

        i = find_pivot(nums, 0, len(nums) - 1)

        lidx = bisearch(nums[:i + 1], target)
        ridx = bisearch(nums[i + 1:], target)
        if lidx != -1:
            return lidx
        if ridx != -1:
            return ridx + i + 1
        return -1


stime = time.time()
# print(0 == Solution().search([4,5,6,7,0,1,2], 4))
# print(4 == Solution().search([4,5,6,7,0,1,2], 0))
# print(-1 == Solution().search([1], 0))
# print(-1 == Solution().search([1, 3], 0))
# print(5 == Solution().search([3, 4, 5, 6, 1, 2], 2))
# print(6 == Solution().search([4,5,6,7,8,9,1,2,3], 1))
# print(0 == Solution().search([5,1,3], 5))
# print(2 == Solution().search([1,3,5], 5))
print(3 == Solution().search([7, 8, 1, 2, 3, 4, 5, 6], 2))
print('elapse time: {} sec'.format(time.time() - stime))

