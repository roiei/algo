
import math
import heapq
import time
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1


stime = time.time()
print(4 == Solution().search([-1,0,3,5,9,12], 9))
print(-1 == Solution().search([-1,0,3,5,9,12], 2))
print('elapse time: {} sec'.format(time.time() - stime))

