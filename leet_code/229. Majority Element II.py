import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        n = len(nums)
        thr = n//3
        nums.sort()
        res, freq, pre = [], 0, -1
        for num in nums:
            if pre != num:
                freq = 1
            else:
                freq += 1
            if freq > thr and num not in res:
                res += num,
            pre = num
        return res

    def majorityElement(self, nums):
        if not nums:
            return []
        n = len(nums)
        freq = collections.defaultdict(int)
        s = set(nums)
        for num in nums:
            freq[num] += 1
        return [k for k, v in freq.items() if v > n//3]

    
stime = time.time()
print(Solution().majorityElement([3,2,3]))
print('elapse time: {} sec'.format(time.time() - stime))