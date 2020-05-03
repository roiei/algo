
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator
import bisect


class Solution:
    def smallerNumbersThanCurrent(self, nums: [int]) -> [int]:
        nums = list(zip(range(len(nums)), nums))
        nums = sorted(nums, key=lambda p: p[1])

        res = [0]*len(nums)
        arr = []
        for i, num in enumerate(nums):
            idx = bisect.bisect_left(arr, num[1])
            arr += num[1],
            res[num[0]] = idx

        return res


stime = time.time()
print([4,0,1,1,3] == Solution().smallerNumbersThanCurrent([8,1,2,2,3]))
print([2,1,0,3] == Solution().smallerNumbersThanCurrent([6,5,4,8]))
print([0,0,0,0] == Solution().smallerNumbersThanCurrent([7,7,7,7]))
print('elapse time: {} sec'.format(time.time() - stime))