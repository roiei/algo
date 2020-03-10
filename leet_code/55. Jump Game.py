import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) <= 1:
            return True
        
        step = nums[0] - 1
        
        for i in range(1, len(nums)-1):
            if step < 0:
                break
            step = max(step, nums[i]) - 1
        
        return True if step >= 0 else False


stime = time.time()
print(False == Solution().canJump([0,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))