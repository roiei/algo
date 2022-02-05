import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def comb(start, r, seq, res):
            if len(seq) == r:
                all_or = 0
                for num in seq:
                    all_or |= num
                res += all_or,
                return
        
            for i in range(start, len(nums)):
                comb(i + 1, r, seq + [nums[i]], res)
        
        res = []
        for i in range(1, len(nums) + 1):
            comb(0, i, [], res)

        all_or = 0
        for num in nums:
            all_or |= num

        cnt = 0
        for seq in res:
            if all_or == seq:
                cnt += 1

        return cnt


stime = time.time()
print(2 == Solution().countMaxOrSubsets(nums = [3,1]))
print(7 == Solution().countMaxOrSubsets(nums = [2,2,2]))
print(6 == Solution().countMaxOrSubsets(nums = [3,2,1,5]))
print('elapse time: {} sec'.format(time.time() - stime))