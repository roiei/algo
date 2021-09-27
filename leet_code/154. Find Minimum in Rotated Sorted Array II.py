import time
from util.util_list import *
from typing import List


class Solution:
    def find_rot_ptr(self, nums, n, l, r):
        if l >= r:
            return -1
        m = (l+r)//2
        if m-1 >= 0:
            if nums[m-1] > nums[m]:
                return m-1
        if nums[m] > nums[m+1]:
            return m
        pv1 = self.find_rot_ptr(nums, n, m+1, r)
        pv2 = self.find_rot_ptr(nums, n, l, m-1)
        if -1 == pv1 and -1 == pv2:
            return -1
        return pv1 if -1 == pv2 else pv2

    def findMin(self, nums: 'List[int]') -> int:
        if not nums:
            return -1
        n = len(nums)
        if 1 == n:
            return nums[0]
        if 2 == n:
            return min(nums[0], nums[1])
        pv = self.find_rot_ptr(nums, n, 0, n-1)
        if -1 != pv:
            return nums[pv+1]
        return nums[0]


    def findMin(self, nums: [int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def find_pivot(nums, l, r):
            if l >= r:
                return -1
            m = (l + r)//2
            if m-1 >= 0 and nums[m-1] > nums[m]:
                return m-1
            if nums[m] > nums[m+1]:
                return m
            
            ret = find_pivot(nums, l, m-1)
            if -1 != ret:
                return ret
            return find_pivot(nums, m+1, r)
    
        idx = find_pivot(nums, 0, n-1)
        if -1 == idx:
            return nums[0]
        return min(nums[0], nums[idx+1])

    def findMin(self, nums: [int]) -> int:
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
        if i == -1:
            return nums[0]

        return nums[i + 1]


stime = time.time()
#print(Solution().findMin([3,4,5,1,2] ))
#print(Solution().findMin([1,2,3,4,5,6]))
print(1 == Solution().findMin([3,1,1]))
#print(Solution().findMin([2,3,4,5,1]))
print('elapse time: {} sec'.format(time.time() - stime))