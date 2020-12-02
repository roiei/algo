import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0

        def rob1(nums):
            nums = [0]*2 + nums
            mx = 0

            for i in range(2, len(nums)):
                mx = max(mx, nums[i - 2])
                nums[i] += mx

            return max(nums)

        return max(rob1(nums[:-1]), rob1(nums[1:]), *nums)


stime = time.time()
print(3 == Solution().rob([2,3,2]))
print(4 == Solution().rob([1,2,3,1]))
print('elapse time: {} sec'.format(time.time() - stime))