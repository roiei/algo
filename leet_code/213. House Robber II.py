import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if 1 == n:
            return nums[0]
        mx = 0
        nums1 = [0]*2 + nums[:n-1]
        nums2 = [0]*2 + nums[1:]
        for i in range(2, len(nums1)):
            mx = max(nums1[i-2], mx)
            nums1[i] = max(nums1[i-2]+nums1[i], mx+nums1[i])
        mx = 0
        for i in range(2, len(nums2)):
            mx = max(nums2[i-2], mx)
            nums2[i] = max(nums2[i-2]+nums2[i], mx+nums2[i])
        return max(max(nums1), max(nums2))

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        def get_max(nums):
            n = len(nums)        
            dp = [0]*2 + [0]*n
            mx = 0
            for i in range(2, n+2):
                mx = max(dp[i-2], mx)
                dp[i] = max(dp[i-2] + nums[i-2], mx + nums[i-2])
            return max(dp)
        return max(get_max(nums[1:]), get_max(nums[:len(nums)-1]))


stime = time.time()
print(Solution().rob([2,3,2]))
print(Solution().rob([1,2,3,1]))
print('elapse time: {} sec'.format(time.time() - stime))