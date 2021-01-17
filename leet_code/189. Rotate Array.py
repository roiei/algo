import time
from util.util_list import *
from typing import List


class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        if k > n:
            k = k%n
        if n <= 1:
            return
        if n == k:
            return
        move = nums[n-k:]
        for i in range(n-1, k-1, -1):
            nums[i] = nums[i-k]
        for i in range(len(move)):
            nums[i] = move[i]

    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)

        def reverse(l, r, nums):
            n = r - l + 1
            
            for i in range(n//2):
                nums[l + i], nums[r - i] = nums[r - i], nums[l + i]
        
        reverse(0, len(nums) - 1, nums)
        reverse(0, k - 1, nums)
        reverse(k, len(nums) - 1, nums)


stime = time.time()
print([5,6,7,1,2,3,4] == Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3))
print('elapse time: {} sec'.format(time.time() - stime))