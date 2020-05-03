
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


class Solution:
    def createTargetArray(self, nums: [int], index: [int]) -> [int]:
        res = []
        for num, idx in zip(nums, index):
            res.insert(idx, num)

        return res





stime = time.time()
print([0,4,1,3,2] == Solution().createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))