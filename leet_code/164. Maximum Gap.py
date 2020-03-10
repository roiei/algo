
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        nums.sort()
        mx = 0
        
        for i in range(len(nums) - 1):
            diff = nums[i + 1] - nums[i]
            mx = max(mx, diff)
        return mx


stime = time.time()
print(3 == Solution().maximumGap([3,6,9,1]))
print('elapse time: {} sec'.format(time.time() - stime))