import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def triangleNumber(self, nums):
        res = 0
        if len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res

    def triangleNumber(self, nums):
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] > nums[k] and 
                        nums[i] + nums[k] > nums[j] and 
                        nums[j] + nums[k] > nums[i]):
                        cnt += 1
        return cnt


stime = time.time()
print(Solution().triangleNumber([2,2,3,4]))
print('elapse time: {} sec'.format(time.time() - stime))