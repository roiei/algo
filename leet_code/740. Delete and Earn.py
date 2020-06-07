
import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import bisect
import collections


class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        def dfs(nums, inc, seq):
            if not nums:
                return inc
            
            res = []
            for i in range(len(nums)):
                inc += nums[i]
                seq += nums[i],
                new_nums = nums[:i] + nums[i + 1:]
                
                while new_nums and nums[i] - 1 in new_nums:
                    idx = new_nums.index(nums[i] - 1)
                    new_nums.pop(idx)
                    
                while new_nums and nums[i] + 1 in new_nums:
                    idx = new_nums.index(nums[i] + 1)
                    new_nums.pop(idx)
                res += dfs(new_nums, inc, seq),

                inc -= nums[i]
                seq.pop()
            
            return max(res)
    
        return dfs(nums, 0, [])
                
                

stime = time.time()
print(6 == Solution().deleteAndEarn([3, 4, 2]))
print('elapse time: {} sec'.format(time.time() - stime))

