import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        diffs = {}
        diffs[0] = -1
        mlen = zeros = ones = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1
            diff = zeros - ones
            if diff in diffs:
                mlen = max(mlen, i - diffs[diff])
            else:
                diffs[diff] = i
        return mlen
                
            

stime = time.time()
print(2 == Solution().findMaxLength([0,1]))
#print(6 == Solution().findMaxLength([0,0,1,0,0,0,1,1]))
print('elapse time: {} sec'.format(time.time() - stime))