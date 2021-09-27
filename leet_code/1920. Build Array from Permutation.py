import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]


stime = time.time()
print([0,1,2,4,5,3] == Solution().buildArray([0,2,1,5,3,4]))
print('elapse time: {} sec'.format(time.time() - stime))