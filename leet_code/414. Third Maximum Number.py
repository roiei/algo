import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect


"""
Given a non-empty array of integers, 
return the third maximum number in this array. 
If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
"""


class Solution:
    def thirdMax(self, nums: [int]) -> int:
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

    def thirdMax(self, nums: [int]) -> int:
        """
            2, 2, 3, 1
            --
            [2]

            2, 2, 3, 1
               --
            [2]

            2, 2, 3, 1
                  --
            [3, 2]

            2, 2, 3, 1
                     --
            [3, 2, 1]
        """

        snums = []
        for num in nums:
            if num in snums:
                continue

            idx = bisect.bisect_left(snums, num)
            snums.insert(idx, num)

        return snums[len(snums) - 3] if len(snums) >= 3 else snums[-1] if snums else -1


stime = time.time()
print(1 == Solution().thirdMax([3, 2, 1]))
print(2 == Solution().thirdMax([1, 2]))
print(1 == Solution().thirdMax([2, 2, 3, 1]))
print(2 == Solution().thirdMax([1,2,2,5,3,5]))
print('elapse time: {} sec'.format(time.time() - stime))