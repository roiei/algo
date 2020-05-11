
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums:
            return True

        pos = nums.index(1)
        for i in range(pos + 1, len(nums)):
            if nums[i] == 1:
                if i - pos <= k:
                    return False
                pos = i
        
        return True
        

stime = time.time()
print(False  == Solution().kLengthApart(nums = [1,0,0,1,0,1], k = 2))
print('elapse time: {} sec'.format(time.time() - stime))