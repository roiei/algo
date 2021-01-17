import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        seq = []
        mn = float('inf')
        tot = 0
        for i, num in enumerate(nums):
            seq += (num, i),
            tot += num
            
            while tot >= s:
                val, i = seq.pop(0)
                tot -= val
                if not seq:
                    l = 1
                else:
                    l = seq[-1][1] - i + 1
                mn = min(mn, l)
            
        return mn if mn != float('inf') else 0


    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        mn = float('inf')
        l = tot = 0
        
        for i, num in enumerate(nums):
            tot += num
            
            while tot >= s:
                tot -= nums[l]
                length = i - l + 1
                mn = min(mn, length)
                l += 1
            
        return mn if mn != float('inf') else 0


    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        mn = float('inf')
        
        l = r = 0
        tot = 0
        
        while r < len(nums):
            tot += nums[r]
            
            while tot >= s:
                mn = min(mn, r - l + 1)
                tot -= nums[l]
                l += 1
            
            r += 1
        
        return mn if mn != float('inf') else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = r = 0
        inc = 0
        mn = float('inf')

        while r < len(nums):
            inc += nums[r]

            while inc >= s:
                mn = min(mn, r - l + 1)
                inc -= nums[l]
                l += 1

            r += 1

        return 0 if mn == float('inf') else mn



stime = time.time()
print(2 == Solution().minSubArrayLen(7, [2,3,1,2,4,3]))
print('elapse time: {} sec'.format(time.time() - stime))