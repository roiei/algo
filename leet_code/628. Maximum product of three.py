import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return reduce(lambda x, y: x*y, nums)
        
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


stime = time.time()
print([1,2,3,1] == Solution().distributeCandies(7, 4))
print('elapse time: {} sec'.format(time.time() - stime))