import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        
        def perm(selected, res, nums):
            if len(selected) == len(nums):
                res += selected[:],
                return
            for num in nums:
                if num in selected:
                    continue
                
                selected += num,
                perm(selected, res, nums)
                selected.pop(selected.index(num))
            
        res = []
        perm([], res, nums)
        for r in res:
            print(r)
        return res
            


stime = time.time()
print(Solution().permute([1,2,3,4,5]))
print('elapse time: {} sec'.format(time.time() - stime))