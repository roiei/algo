import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findLengthOfLCIS(self, nums: [int]) -> int:
        if not nums:
            return 0
        mlen = clen = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                clen += 1
            else:
                mlen = max(mlen, clen)
                clen = 1
        return max(mlen, clen)


stime = time.time()
print(3 == Solution().findLengthOfLCIS([1,3,5,4,7]))
print('elapse time: {} sec'.format(time.time() - stime))