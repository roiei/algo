import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(depth, trace, start, res):
            if depth == 0:
                res += trace,
                return 

            for i in range(start, len(nums)):
                dfs(depth - 1, trace + [nums[i]], i + 1, res)

        res = []
        for k in range(len(nums) + 1):
            dfs(k, [], 0, res)

        return res


stime = time.time()
print([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]] == Solution().subsets([1, 2, 3]))
print('elapse time: {} sec'.format(time.time() - stime))