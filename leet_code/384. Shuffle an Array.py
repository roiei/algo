import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools



class Solution:
    def __init__(self, nums: [int]):
        self.nums = nums

    def reset(self) -> [int]:
        return self.nums
        

    def shuffle(self) -> [int]:
        return random.sample(self.nums, len(self.nums))


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))

     