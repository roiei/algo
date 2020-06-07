import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def __init__(self, w: List[int]):
        self.nums = []
        inc = 0
        for val in w:
            inc += val
            self.nums += inc,

    def pickIndex(self) -> int:
        idx = random.randint(1, self.nums[-1])
        return bisect.bisect_left(self.nums, idx)
        


stime = time.time()
print('elapse time: {} sec'.format(time.time() - stime))

     