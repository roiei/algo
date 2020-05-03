
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def numTeams(self, rating: [int]) -> int:
        def dfs(nums, l, r, prev, cnt, seq):
            if cnt >= 3:
                return 1
        
            res = 0
            for i in range(l, r + 1):
                if nums[i] > prev:
                    res += dfs(nums, i + 1, r, nums[i], cnt + 1, seq + [nums[i]])
            
            return res
            
        res = dfs(rating, 0, len(rating) - 1, float('-inf'), 0, [])
        res += dfs(rating[::-1], 0, len(rating) - 1, float('-inf'), 0, [])
        return res





stime = time.time()
print(3 == Solution().numTeams(rating = [2,5,3,4,1]))
print(0 == Solution().numTeams([2,1,3]))
print(4 == Solution().numTeams([1,2,3,4]))
print('elapse time: {} sec'.format(time.time() - stime))