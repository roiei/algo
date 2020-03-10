import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def medianSlidingWindow(self, nums: [int], k: int) -> [float]:
        def search(nums, r, val):
            l = 0
            while l <= r:
                m = (l + r)//2
                if nums[m] == val:
                    return m
                if nums[m] < val:
                    l = m + 1
                else:
                    r = m - 1
            return l
            
        n = len(nums)
        is_even = True if k%2 == 0 else False
        if n < k:
            if is_even:
                return sum(nums)//n
            return nums[n//2]
    
        wnd = [0]*k
        for i in range(k):
            wnd[i] = nums[i]
        wnd.sort()
        out = []
        
        if is_even:
            out += float((wnd[k//2] + wnd[k//2-1])/2),
        else:
            out += float(wnd[k//2]),
        
        for i in range(1, n-k+1):
            idx = search(wnd, k-1, nums[i-1])
            wnd.pop(idx)
            idx = search(wnd, k-2, nums[i+k-1])
            wnd.insert(idx, nums[i+k-1])
            if is_even:
                out += float((wnd[k//2] + wnd[k//2-1])/2),
            else:
                out += float(wnd[k//2]),
        return out

    from bisect import bisect_left 


    def medianSlidingWindow(self, nums: [int], k: int) -> [float]:
        n = len(nums)
        is_even = True if k%2 == 0 else False
        if n < k:
            if is_even:
                return sum(nums)//n
            return nums[n//2]
    
        wnd = [0]*k
        for i in range(k):
            wnd[i] = nums[i]
        wnd.sort()
        out = []
        
        if is_even:
            out += (wnd[k//2] + wnd[k//2-1])/2,
        else:
            out += float(wnd[k//2]),
        
        for i in range(1, n-k+1):
            wnd.pop(bisect_left(wnd, nums[i-1]))
            wnd.insert(bisect_left(wnd, nums[i+k-1]), nums[i+k-1])
            if is_even:
                out += (wnd[k//2] + wnd[k//2-1])/2,
            else:
                out += float(wnd[k//2]),
        return out


stime = time.time()
#print([1,-1,-1,3,5,6] == Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
#print([1073741824.0, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1073741827.0] == Solution().medianSlidingWindow([2147483647,1,2,3,4,5,6,7,2147483647], 2))
print([8.0,6.0,8.0,8.0,5.0] == Solution().medianSlidingWindow([7,0,3,9,9,9,1,7,2,3], 6))
print('elapse time: {} sec'.format(time.time() - stime))