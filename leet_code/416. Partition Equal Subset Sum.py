import time
from util.util_list import *
from util.util_tree import *
import copy
import heapq
import collections


class Solution:
    def canPartition(self, nums) -> bool:
        def dfs(start, target):
            if target == 0:
                return True
            if target < 0:
                return False
            if start == n:
                return False
            if (start, target) in mem:
                return mem[(start, target)]
            for i in range(start, n):
                if True == dfs(i+1, target-nums[i]):
                    mem[(start, target)] = True
                    return True
            mem[(start, target)] = False
            return False
              
        n = len(nums)
        half = sum(nums)
        if 0 != half%2:
            return False
        mem = {}
        return dfs(0, half//2)

    def canPartition(self, nums) -> bool:
        def dfs(start, target):
            if target == 0:
                return True
            if target < 0:
                return False
            if start == n:
                return False
            if (start, target) in mem:
                return mem[(start, target)]
            res = []
            for i in range(start, n):
                res += dfs(i+1, target-nums[i]),
            mem[(start, target)] = any(res)
            return mem[(start, target)]
              
        n = len(nums)
        half = sum(nums)
        if 0 != half%2:
            return False
        mem = {}
        return dfs(0, half//2)
            
            
stime = time.time()
print(True == Solution().canPartition([1, 5, 11, 5]))
print(False == Solution().canPartition([1, 2, 3, 5]))
print('elapse time: {} sec'.format(time.time() - stime))

     