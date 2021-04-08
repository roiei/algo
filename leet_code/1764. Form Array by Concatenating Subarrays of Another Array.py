import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0

        for group in groups:
            for i in range(start, len(nums)):
                if nums[i:i + len(group)] == group:
                    start = i + len(group)
                    break
            else:
                return False

        return True


stime = time.time()
print(True == Solution().canChoose(groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]))
print('elapse time: {} sec'.format(time.time() - stime))
