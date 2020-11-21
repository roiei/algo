import time
from util.util_list import *
from util.util_tree import *
import copy
import functools
import collections


# Given an array nums and an integer target.
# Return the maximum number of non-empty non-overlapping subarrays
# such that the sum of values in each subarray is equal to target


class Solution:
    def maxNonOverlapping(self, nums: [int], target: int) -> int:
        def dfs(l, r, inc, cnt, seq):
            nonlocal mx

            if inc == target and seq:
                seq = []
                cnt += 1

            if inc >= target:
                inc = 0

            if l >= r:
                mx = max(cnt, mx)
                return 0

            cmx = cnt
            for i in range(l, r):
                cmx = max(cmx, dfs(i + 1, r, inc + nums[i], cnt, seq + [nums[i]]))

            return cmx

        mx = 0
        res = dfs(0, len(nums), 0, 0, [])
        print(res)
        return mx

    def maxNonOverlapping(self, nums: [int], target: int) -> int:
        @functools.lru_cache
        def dfs(l, r, inc, cnt, valid):
            nonlocal mx

            if inc == target and valid:
                cnt += 1

            if inc >= target:
                inc = 0

            if l >= r:
                mx = max(cnt, mx)
                return mx

            cmx = 0
            for i in range(l, r):
                if i == l:
                    cmx = max(cmx, dfs(i + 1, r, inc + nums[i], cnt, True))
                else:
                    cmx = max(cmx, dfs(i + 1, r, nums[i], cnt, True))
            return cmx

        mx = 0
        res = dfs(0, len(nums), 0, 0, False)
        print(res, mx)
        return mx


    def maxNonOverlapping(self, nums: [int], target: int) -> int:
        hs = {0}
        inc = 0
        cnt = 0

        for num in nums:
            inc += num

            if inc - target in hs:
                hs = {0}
                inc = 0
                cnt += 1
            else:
                hs.add(inc)

        return cnt


stime = time.time()
print(2 == Solution().maxNonOverlapping([2,2,3,3,-3,-1,2,-3], 4))
# print(3 == Solution().maxNonOverlapping(nums = [-2,6,6,3,5,4,1,2,8], target = 10))
# print(2 == Solution().maxNonOverlapping(nums = [1,1,1,1,1], target = 2))
# print(2 == Solution().maxNonOverlapping(nums = [-1,3,5,1,4,2,-9], target = 6))
# print(3 == Solution().maxNonOverlapping(nums = [0,0,0], target = 0))


print('elapse time: {} sec'.format(time.time() - stime))