import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findTargetSumWays(self, nums: [int], S: int) -> int:
        cache = {}
        def dfs(nums, i, n, s):
            if (s, i, n) in cache:
                return cache[(s, i, n)]
            if i == n:
                if s == S:
                    return 1
                return 0
            res = dfs(nums, i+1, n, s+nums[i])
            res += dfs(nums, i+1, n, s-nums[i])
            cache[(s, i, n)] = res
            return res
        
        res = dfs(nums, 0, len(nums), 0)
        return res

    def findTargetSumWays(self, nums: [int], S: int) -> int:
        s = sum(nums)
        n, m = len(nums), 2*s + 1
        if s < S:
            return 0

        dp = [[0]*m for _ in range(n+1)]
        dp[0][s] = 1

        for i in range(n):
            for j in range(nums[i], m - nums[i]):
                if dp[i][j]:
                    dp[i+1][j+nums[i]] += dp[i][j]
                    dp[i+1][j-nums[i]] += dp[i][j]
        return dp[-1][s+S]

    def findTargetSumWays(self, nums: [int], S: int) -> int:
        def dfs(nums, l, r, inc):
            if (l, r, inc) in mem:
                return mem[(l, r, inc)]

            if l > r:
                if inc == S:
                    return 1
                return 0

            cnt = dfs(nums, l + 1, r, inc + nums[l]) +
                  dfs(nums, l + 1, r, inc - nums[l])

            mem[(l, r, inc)] = cnt
            return cnt

        mem = {}
        return dfs(nums, 0, len(nums) - 1, 0)

            

stime = time.time()
#print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
print(Solution().findTargetSumWays([8, 3, 5, 7, 3, 4], 0))

print('elapse time: {} sec'.format(time.time() - stime))