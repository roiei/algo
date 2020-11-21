
import math
import heapq
import time


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

    def search(self, nums: 'List[int]', target: int) -> bool:
        if not nums:
            return False
        n = len(nums)
        idx = self.find_rot_ptr(nums, 0, n-1)
        if -1 != idx and nums[idx] == target: # code below ignores pivot
            return True
        res = -1
        if -1 != idx:
            left = nums[:idx]
            nleft = len(left)
            r1 = self.binary_search(left, nleft, target)
            right = nums[idx+1:]
            nright = len(right)
            r2 = self.binary_search(right, nright, target)
            #print('r1 = {}, r2 = {}'.format(r1, r2))
            return True if -1 != r1 or -1 != r2 else False
        else:
            return True if -1 != self.binary_search(nums, n, target) else False

    def search(self, nums: [int], target: int) -> bool:
        if not nums:
            return False

        def search(nums, target):
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

        def dfs(l, r):
            if l > r:
                return -1

            m = (l + r)//2
            if m - 1 >= 0 and nums[m - 1] > nums[m]:
                return m
            elif m + 1 <= r and nums[m] > nums[m + 1]:
                return m + 1

            lidx = dfs(l, m - 1)
            if -1 != lidx:
                return lidx
            ridx = dfs(m + 1, r)
            if -1 != ridx:
                return ridx
            return -1
        
        pivot_idx = dfs(0, len(nums) - 1)
        if -1 == pivot_idx:
            return True if -1 != search(nums, target) else False
        
        idx = search(nums[:pivot_idx], target)
        if -1 != idx:
            return True
        idx = search(nums[pivot_idx:], target)
        if -1 != idx:
            return True
        return False


stime = time.time()
#print(Solution().search([2,5,6,0,0,1,2], 0))
#print(Solution().search([2,5,6,0,0,1,2], 3))
print(Solution().search([3, 1], 1))
print('elapse time: {} sec'.format(time.time() - stime))

