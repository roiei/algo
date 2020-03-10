
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution(object):
    def maxSubArrayLen(self, nums : 'an array', k : 'a target value') -> 'maximum length of a subarray that sums to k':
        idxs = collections.defaultdict(int)
        idxs[0] = -1
        tot = res = 0
     
        for i in range(len(nums)):
            tot += nums[i]
            if tot - k in idxs:
                res = max(res, i - idxs[tot - k])
        
            if tot not in idxs:
                idxs[tot] = i

        return res


stime = time.time()
print(4 == Solution().minSubArrayLen([1, -1, 5, -2, 3], 3))
print(2 == Solution().minSubArrayLen([-2, -1, 2, 1], 1))
print('elapse time: {} sec'.format(time.time() - stime))