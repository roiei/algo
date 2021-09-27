import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        l = 0
        r = len(nums)-1
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort(key=lambda p:p[0])
        while l < r:
            tot = nums[l][0]+nums[r][0]
            if target == tot:
                return [nums[l][1], nums[r][1]] if nums[l][1] < nums[r][1] else [nums[r][1], nums[l][1]]
            if target < tot:
                r -= 1
            else:
                l += 1
        return [nums[l][1], nums[r][1]] if nums[l][1] < nums[r][1] else [nums[r][1], nums[l][1]]

    def twoSum(self, nums: [int], target: int) -> [int]:
        n = len(nums)
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort(key=lambda p:p[0])

        def search(nums, l, r, target):
            while l <= r:
                m = (l+r)//2
                if target == nums[m][0]:
                    return m
                if target > nums[m][0]:
                    l = m+1
                else:
                    r = m-1
            return l

        for i in range(n-1):
            idx = search(nums, i+1, n-1, target-nums[i][0])
            if idx > n-1:
                idx = n-1
            if target == nums[i][0]+nums[idx][0]:
                return [nums[i][1], nums[idx][1]] if nums[i][1] < nums[idx][1] else [nums[idx][1], nums[i][1]]
        return [-1, -1]


    def twoSum(self, nums: [int], target: int) -> [int]:
        
        def search(nums, l, target):
            r = len(nums) - 1
            
            while l <= r:
                m = (l + r)//2
                if nums[m][0] == target:
                    return m
                
                if nums[m][0] > target:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1
        
        snums = [(num, i) for i, num in enumerate(nums)]
        snums.sort(key=lambda p:p[0], reverse=False)
        
        for i, num in enumerate(snums):
            m = search(snums, i + 1, target - num[0])
            if -1 != m:
                return [snums[i][1], snums[m][1]]
        
        return [-1, -1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(i, num) for i, num in enumerate(nums)]
        nums.sort(key=lambda p: p[1])

        def search(nums, l, r, val):
            while l <= r:
                m = (l + r)//2
                if nums[m][1] == val:
                    return m
                if nums[m][1] > val:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1
            
        for i in range(len(nums)):
            idx = search(nums, i + 1, len(nums) - 1, target - nums[i][1])
            if idx != -1:
                return [nums[i][0], nums[idx][0]]
        
        return [-1, -1]


stime = time.time()
print([0,3] == Solution().twoSum([0,4,3,0], 0))
# print([1,2] == Solution().twoSum([3,2,4], 6))
#print(Solution().twoSum([3,2,3], 6))
# print([2,4] == Solution().twoSum([-1,-2,-3,-4,-5], -8))
#print(Solution().twoSum([-3,4,3,90], 0))
print('elapse time: {} sec'.format(time.time() - stime))