
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List



class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        mx = [0]*len(nums)
        mn = [0]*len(nums)
        
        mx[0] = nums[0]
        for i in range(1, len(nums)):
            mx[i] = max(mx[i - 1], nums[i])
        
        mn[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            mn[i] = min(mn[i + 1], nums[i])
        
        score = 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] < nums[i + 1]:
                if mx[i - 1] < nums[i] < mn[i + 1]:
                    score += 2
                else:
                    score += 1

        return score


stime = time.time()
print(2 == Solution().sumOfBeauties([1,2,3]))
print(2 == Solution().sumOfBeauties([6,8,3,7,8,9,4,8]))
print('elapse time: {} sec'.format(time.time() - stime))