import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, -num)
        
        val = -1
        while k:
            val = heapq.heappop(q)
            k -= 1

        return -1*val

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


stime = time.time()
print(5 == Solution().findKthLargest([3,2,1,5,6,4], 2))
print('elapse time: {} sec'.format(time.time() - stime))
