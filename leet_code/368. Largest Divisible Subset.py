
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        
        n = len(nums)
        dp = [[num] for num in nums]

        for i in range(n - 1):
            for j in range(i + 1, n):
                if not nums[j]%nums[i] and len(dp[i]) >= len(dp[j]):
                    dp[j] = dp[i] + [nums[j]]

        dp.sort(key = len)
        return dp and dp[-1]


    def largestDivisibleSubset2(self, nums):
        if not nums:
            return []

        nums.sort()
        dp = collections.defaultdict(list)
        for num in nums:
            dp[num] += num,
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if 0 != nums[j]%nums[i]:
                    continue
                
                if len(dp[nums[i]]) + 1 >= len(dp[nums[j]]):
                    dp[nums[j]] = dp[nums[i]] + [nums[j]]
        
        dp = sorted(dp.items(), key=lambda p: len(p[1]), reverse=True)
        return dp[0][1]


stime = time.time()
#print([1,3] == Solution().largestDivisibleSubset([1,2,3]))
print([4,8,240] == Solution().largestDivisibleSubset([4,8,10,240]))
#print([1,2,4,8] == Solution().largestDivisibleSubset([1,2,4,8]))
print('elapse time: {} sec'.format(time.time() - stime))