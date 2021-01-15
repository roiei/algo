
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
from typing import List
import bisect


"""
    1 , 2 , 2 , 2 , 5 , 0

"""

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        n = len(nums)
        cnt = 0

        def dfs(ls, ms, rs, i, j):
            nonlocal cnt

            if ls <= ms <= rs:
                if (i, j) not in visited:
                    cnt += 1
                    visited.add((i, j))

            if j == n:
                return

            if i + 1 < j:
                dfs(ls + nums[i], ms - nums[i], rs, i + 1, j)

            if j < n - 1:
                dfs(ls, ms + nums[j], rs - nums[j], i, j + 1)

        visited = set()
        dfs(nums[0], nums[1], sum(nums) - nums[0] - nums[1], 1, 2)
        return cnt



stime = time.time()
# print(3 == Solution().waysToSplit([1,2,2,2,5,0]))
# print(0 == Solution().waysToSplit([3,2,1]))
# print(1 == Solution().waysToSplit([1,1,1]))
print(3 == Solution().waysToSplit([2,3,5,10]))


print('elapse time: {} sec'.format(time.time() - stime))