import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


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

    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums) + 2)
        
        for i in range(len(nums)):
            dp[i + 2] = max(nums[i] + dp[i], dp[i + 1])
        
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        mx = 0
        nums = [0]*2 + nums

        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], mx)
            mx = max(mx, nums[i])

        return mx


stime = time.time()
print(4 == Solution().rob([1,2,3,1]))
print(12 == Solution().rob([2,7,9,3,1]))
print(4 == Solution().rob([2, 1, 1, 2]))
print('elapse time: {} sec'.format(time.time() - stime))