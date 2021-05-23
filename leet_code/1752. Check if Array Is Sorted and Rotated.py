import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def check(self, nums: List[int]) -> bool:
        pre = nums[-1]
        idx = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < pre:
                pre = nums[i]
                continue
            
            if nums[i] == pre:
                continue
            
            idx = i + 1
            break
        
        return sorted(nums) == nums[idx:] + nums[:idx]
