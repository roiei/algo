import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        mx = 0
        nums = [0]*2 + nums
        for i in range(2, len(nums)):
            mx = max(nums[i-2], mx)
            nums[i] = max(nums[i-2]+nums[i], mx+nums[i])
        return max(nums)



stime = time.time()
print(Solution().rob([1,2,3,1]))
print('elapse time: {} sec'.format(time.time() - stime))