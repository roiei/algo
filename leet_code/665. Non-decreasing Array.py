import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def checkPossibility(self, nums: [int]) -> bool:
        allowed = True
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if not allowed:
                    return False
                allowed = False
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True

    def checkPossibility(self, nums: [int]) -> bool:
        n = len(nums)
        dec = 1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if dec > 0:
                    dec -= 1
                else:
                    return False
        return True



stime = time.time()
# print(True == Solution().checkPossibility([4,2,3]))
# print(False == Solution().checkPossibility([4,2,1]))
print(False == Solution().checkPossibility([3,4,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))