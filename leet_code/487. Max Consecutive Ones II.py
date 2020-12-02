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

    def findMaxConsecutiveOnes2(self, nums):
        
        mx = 0
        seq = []
        
        for num in nums:
            if num == 0 and 0 in seq:
                seq = seq[seq.index(0) + 1:]
            
            seq += num,
            mx = max(mx, len(seq))
        
        return mx

    def findMaxConsecutiveOnes(self, nums):
        mx = 0
        seq = ''

        for i, num in enumerate(nums):
            if num == 0:
                seq = seq[seq.find('0') + 1:]

            seq += str(num)
            mx = max(mx, len(seq))

        return mx
    
    # 1,0,1,0,1
    # 1
    # -> wnd = [1]
    
    # 0
    # [1] + [0] -> wnd = [1, 0]

    # 1
    # -> wnd = [1, 0, 1]

    # 0
    # drop until '0' in wnd
    # -> wnd = [1] + [0] = [1, 0]

    # 1
    # -> wnd = [1, 0, 1]


    def findMaxConsecutiveOnes(self, nums):
        wnd = []
        n = len(nums)
        mx = 0
        i = 0

        while i < n:
            if nums[i] == 0:
                idx = 0
                found = False
                while idx < len(wnd):
                    if wnd[idx] == 0:
                        found = True
                        break
                    idx += 1

                if found:
                    wnd = wnd[idx + 1:]

            wnd += nums[i],
            mx = max(mx, len(wnd))
            i += 1

        return mx


stime = time.time()
print(4 == Solution().findMaxConsecutiveOnes([1,0,1,1,0]))
print(3 == Solution().findMaxConsecutiveOnes([1,0,1,0,1]))
print(14 == Solution().findMaxConsecutiveOnes([1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,0,1,1,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1]))
print('elapse time: {} sec'.format(time.time() - stime))