import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def rob(self, nums):
        # 0   0   2   1   1   2
        #        ---
        # mx = max(0, nums[i - 2]) = 0
        # nums[i] += max(nums[i - 2], mx = 2
        #
        # 0   0   2   1   1   2
        #            ---
        # mx = max(mx, 0) = 0
        # nums[i] += max(nums[i - 2], mx) = 1
        #
        # 0   0   2   1   1   2
        #                ---
        # mx = max(mx, 2) = 2
        # nums[i] += max(nums[i - 2], mx) = 3
        #
        # 0   0   2   1   3   2
        #                    ---
        # mx = max(mx, 1) = 2
        # nums[i] += max(nums[i - 2], mx) = 4

        nums = [0]*2 + nums
        mx = 0

        for i in range(2, len(nums)):
            mx = max(nums[i - 2], mx)
            nums[i] += mx

        return max(nums)


stime = time.time()
print(4 == Solution().rob([1,2,3,1]))
print(12 == Solution().rob([2,7,9,3,1]))
print(4 == Solution().rob([2, 1, 1, 2]))
print('elapse time: {} sec'.format(time.time() - stime))