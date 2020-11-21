import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections
import functools
import bisect


class Solution:
    def longestSubarray(self, nums: [int]) -> int:
        last = 0
        zero = -1
        seq = []
        
        for i, num in enumerate(nums):
            if num == 0:
                last = zero + 1
                zero = i
            
            seq += i - last,

        return max(seq)


stime = time.time()
print(3 == Solution().longestSubarray(nums = [1,1,0,1]))
print(5 == Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))
print(2 == Solution().longestSubarray(nums = [1,1,1]))
print(4 == Solution().longestSubarray(nums = [1,1,0,0,1,1,1,0,1]))
print('elapse time: {} sec'.format(time.time() - stime))

