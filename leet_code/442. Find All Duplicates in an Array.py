import time
from util.util_list import *
from util.util_tree import *
import copy
import collections


# O(1) space, O(n) time
class Solution:
    def findDuplicates(self, nums: [int]) -> [int]:
        if not nums:
            return []
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        return [k for k, v in freq.items() if v > 1]


    def findDuplicates(self, nums: [int]) -> [int]:
        res = []
        
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            
            if nums[index] < 0:
                res += abs(nums[i]),
            else:
                nums[index] = -(nums[index])

        return res


stime = time.time()
print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
print('elapse time: {} sec'.format(time.time() - stime))