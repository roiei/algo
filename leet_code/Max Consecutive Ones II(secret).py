import time
from util.util_list import *
from util.util_tree import *
import copy
import collections

    
class Solution:
    """
    @param nums: a list of integer
    @return: return a integer, denote  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        
        stk = [0]
        mlen = i = 0
        n = len(nums)
        
        for pos in range(n):
            if nums[pos] == 0:
                i += 1
                stk += i,
                break
            i += 1
        
        for i in range(i, n):
            if nums[i] == 0:
                mlen = max(mlen, i - stk.pop(0))
                stk += i + 1,

        return mlen


stime = time.time()
print(4 == Solution().findMaxConsecutiveOnes([1,0,1,1,0]))
print('elapse time: {} sec'.format(time.time() - stime))