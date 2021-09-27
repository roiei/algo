import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def combinationSum4(self, nums: [int], target: int) -> int:
        def dfs(nums, cur, depth):
            if (depth, cur) in mem:
                return mem[(depth, cur)]
            if cur == 0:
                return 1
            if cur < 0:
                return 0
            res = 0
            for i in range(n):
                res += dfs(nums, cur - nums[i], depth+1)
            mem[(depth, cur)] = res
            return res

        n = len(nums)
        mem = {}
        res = dfs(nums, target, 0)
        return res


    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        nums.sort()
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(nums[0], target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i-num]
        return dp[-1]

    def combinationSum4(self, nums, target):
        nums.sort()
        dp = [0]*(target + 1)
        dp[0] = 1

        for i in range(nums[0], target + 1):
            for num in nums:
                if i < num:
                    break

                dp[i] += dp[i - num]

        return dp[-1]


stime = time.time()
print(7 == Solution().combinationSum4([1, 2, 3], 4))
print(5 == Solution().combinationSum4([1, 2], 4))
print('elapse time: {} sec'.format(time.time() - stime))