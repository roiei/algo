
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from functools import lru_cache
import bisect


class Solution:
    def specialArray(self, nums: [int]) -> int:
        vals = []
        n = len(nums)
        nums.sort()
        mn = min(nums)
        mx = max(nums)
        print(nums)

        for i in range(1, mx + 1):
            idx = bisect.bisect_left(nums, i)
            print(i, idx, n - idx)
            cnt = n - idx

            if i == cnt:
                return i

        return -1


stime = time.time()
print(2 == Solution().specialArray([3,5]))
print(-1 == Solution().specialArray([0,0]))
print(3 == Solution().specialArray([0,4,3,0,4]))
print(-1 == Solution().specialArray([3,6,7,7,0]))
print('elapse time: {} sec'.format(time.time() - stime))




# Input: arr = [1,4,2,5,3]
# Output: 58
# Explanation: The odd-length subarrays of arr and their sums are:
# [1] = 1
# [4] = 4
# [2] = 2
# [5] = 5
# [3] = 3
# [1,4,2] = 7
# [4,2,5] = 11
# [2,5,3] = 10
# [1,4,2,5,3] = 15
# If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

