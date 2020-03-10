import time
from util_list import *
from util_tree import *
import copy
import collections


class Solution:
    def circularArrayLoop(self, nums: [int]) -> bool:
        n = len(nums)
        for i, num in enumerate(nums):
            length = 0
            ci = i
            forward = nums[ci] > 0
            while length < n:       # check infinite loop
                
                if (forward and nums[ci] < 0) or (not forward and nums[ci] > 0):
                    break
                if 0 == nums[ci]:
                    break
                nidx = (ci + nums[ci]) % n
                if nidx == ci:      # cycle length must bigger than  1
                    break
                ci = nidx
                if ci == i:
                    return True
                length += 1
        return False


stime = time.time()
print(True == Solution().circularArrayLoop([2,-1,1,2,2]))
print(False == Solution().circularArrayLoop([-1,2]))
print('elapse time: {} sec'.format(time.time() - stime))