import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


stime = time.time()
print(Solution().NumArray([-2, 0, 3, -5, 2, -1]))
print('elapse time: {} sec'.format(time.time() - stime))