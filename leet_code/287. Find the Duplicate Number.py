import time
from util.util_list import *
from util.util_tree import *
import copy
import collections



class Solution:
    def binsert(self, nums, num):
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == num:
                return True, m
            if nums[m] < num:
                l = m+1
            else:
                r = m-1
        return False, l

    def findDuplicate(self, nums) -> int:
        if not nums:
            return None
        snums = []
        for n in nums:
            found, idx = self.binsert(snums, n)
            if False == found:
                snums.insert(idx, n)
            else:
                return n
        return None

    def findDuplicate(self, nums):
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = (l + r)//2

            print(sum(num <= m for num in nums), m)
            
            if sum(num <= m for num in nums) > m:
                r = m - 1
            else:
                l = m + 1

            print('l, r = ', l, r)
        
        return l


stime = time.time()
print(2 == Solution().findDuplicate([1,3,4,2,2]))
#print(Solution().findDuplicate([1,2,3,4,5]))
print('elapse time: {} sec'.format(time.time() - stime))