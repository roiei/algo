import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



# not completed yet
# failed @ 14th TC

class Solution:
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        tgt = target

        is_found = False
        while True:
            if r != l:
                m = (r-l)//2
                m += l
            else:
                m = l
            #print('l = {}, r = {}, m = {}'.format(l, r, m))
            if r == l:
                if nums[l] == tgt:
                    is_found = True
                break
            if nums[m] == tgt:
                is_found = True
                break

            if ((nums[m] > nums[r] and (tgt < nums[r] and tgt <= nums[m])) or 
                (nums[m] < nums[r] and (tgt > nums[m] and tgt <= nums[r]))):
                if m <= r-1:
                    l = m+1
                else:
                    l = m
            elif ((nums[m] >= nums[l] and (tgt <= nums[m] and tgt <= nums[l])) or 
                (nums[m] >= nums[l] and (tgt < nums[m] and tgt >= nums[l]))):
                if m <= 1:
                    r = 0
                else:
                    r = m-1
        if False == is_found:
            m = -1
        return m

    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        
        def find_pivot(nums, l, r):
            if l >= r:
                return -1
            m = (l + r)//2
            if m > 0 and nums[m-1] > nums[m]:
                return m-1
            if nums[m] > nums[m+1]:
                return m
        
            ret = find_pivot(nums, l, m-1)
            if -1 != ret:
                return ret
            return find_pivot(nums, m+1, r)
    
        def search(nums, l, r, target):
            while l <= r:
                m = (l + r)//2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
    
        idx = find_pivot(nums, 0, len(nums)-1)
        if -1 == idx:
            return search(nums, 0, len(nums)-1, target)
        else:
            ret = search(nums, 0, idx, target)
            if -1 != ret:
                return ret
            ret = search(nums, idx+1, len(nums)-1, target)
            return ret


stime = time.time()
print(4 == Solution().search([4,5,6,7,0,1,2], 0))
print('elapse time: {} sec'.format(time.time() - stime))