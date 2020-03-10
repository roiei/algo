import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n < 3:
            return max(nums)
        wnd = [-float('inf')]*3
        for num in nums:
            if num > wnd[0]:
                wnd.pop()
                wnd.insert(0, num)
            elif num == wnd[0]:
                continue
            elif num > wnd[1]:
                wnd.pop()
                wnd.insert(1, num)
            elif num == wnd[1]:
                continue
            elif num > wnd[2]:
                wnd.pop()
                wnd.insert(2, num)
              
        if -float('inf') in wnd:
            return max(wnd)
        return wnd[-1]


stime = time.time()
print(1 == Solution().thirdMax([3, 2, 1]))
print(2 == Solution().thirdMax([1, 2]))
print(1 == Solution().thirdMax([2, 2, 3, 1]))
print('elapse time: {} sec'.format(time.time() - stime))