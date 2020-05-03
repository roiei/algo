
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        r = 1
        cnt = 0
        visited = set()
        
        while l < n and r < n:
            diff = nums[r] - nums[l]
            
            if diff == k and (nums[r], nums[l]) in visited:
                r += 1
                continue
            
            if diff == k:
                cnt += 1
                visited.add((nums[r], nums[l]))
                l += 1
                continue

            if diff == 0 or diff < k:
                r += 1
                continue
            
            if diff > k:
                l += 1

            if l == r:
                r += 1
        
        return cnt
        

stime = time.time()
# print(2 == Solution().findPairs([3, 1, 4, 1, 5], k = 2))
# print(4 == Solution().findPairs([1, 2, 3, 4, 5], k = 1))
# print(0 == Solution().findPairs([1, 3, 1, 5, 4], k = 0))
print(0 == Solution().findPairs([1,2,3,4,5], k = 0))
print('elapse time: {} sec'.format(time.time() - stime))