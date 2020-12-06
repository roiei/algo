import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq



# Input: nums = [3,5,2,6], k = 2
# Output: [2,6]


class Solution:
    def mostCompetitive(self, nums: [int], k: int) -> [int]:
        stk = []
        for i, num in enumerate(nums):
            while stk and stk[-1] > num and len(nums) - 1 - i + len(stk) >= k:
                stk.pop()

            stk += num,

        return stk[:k]


stime = time.time()
print([2,6] == Solution().mostCompetitive([3,5,2,6], k = 2))
print([2,3,3,4] == Solution().mostCompetitive(nums = [2,4,3,3,5,4,9,6], k = 4))
print('elapse time: {} sec'.format(time.time() - stime))
