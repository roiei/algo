
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums.pop() - 1)*(nums.pop() - 1)
        


stime = time.time()
print(12 == Solution().maxProduct([3,4,5,2]))
print('elapse time: {} sec'.format(time.time() - stime))

