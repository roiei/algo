import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        diff = float('inf')
        mn = 0

        nums.sort()
    
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                
                if diff > abs(target - tot):
                    diff = abs(target - tot)
                    mn = tot
                
                if tot == target:
                    return tot
            
                if tot > target:
                    r -= 1
                else:
                    l += 1
        
        return mn


stime = time.time()
print(2 == Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))
print('elapse time: {} sec'.format(time.time() - stime))