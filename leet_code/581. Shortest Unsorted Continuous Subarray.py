import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        snums = sorted(nums)
        mini = float('inf')
        maxi = 0
        for i in range(len(nums)):
            if nums[i] != snums[i]:
                mini = min(mini, i)
                maxi = max(maxi, i)
        return maxi-mini+1 if mini != float('inf') else 0


stime = time.time()
print(3 == Solution().findUnsortedSubarray([1,2,4,5,3]))
#print(0 == Solution().findUnsortedSubarray([1,1]))
# print(3 == Solution().findUnsortedSubarray([2,3,3,2,4]))
# print(2 == Solution().findUnsortedSubarray([1,3,2,4,5]))
# print(4 == Solution().findUnsortedSubarray([1,3,2,2,2]))
# print(0 == Solution().findUnsortedSubarray([1,2,3,4]))
# print(5 == Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print('elapse time: {} sec'.format(time.time() - stime))