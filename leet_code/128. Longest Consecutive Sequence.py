
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = list(set(nums))
        nums.sort()
        
        mx = 0
        pre = nums[0]
        cnt = 1
        
        i = 1
        while i < len(nums):
            if pre + 1 == nums[i]:
                cnt += 1
            else:
                mx = max(mx, cnt)
                cnt = 1
            pre = nums[i]
            i += 1
        
        mx = max(mx, cnt)
        return mx


stime = time.time()
print(4 == Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
print('elapse time: {} sec'.format(time.time() - stime))