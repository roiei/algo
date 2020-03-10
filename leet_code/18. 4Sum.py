
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        n = len(nums)
        res = set()
        nums.sort()

        for i in range(n - 2):
            for j in range(i + 1, n - 2):
                l = j + 1
                r = n - 1

                acc = nums[i] + nums[j]
                diff = target - acc

                while l < r:
                    sum = nums[l] + nums[r]
                    if sum == diff:
                        res.add((nums[i], nums[j], nums[l], nums[r],))
                        l += 1
                        r -= 1
                        continue

                    if sum > diff:
                        r -= 1
                    elif sum < diff:
                        l += 1

        return res


stime = time.time()
print([
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
] == Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print('elapse time: {} sec'.format(time.time() - stime))