import time
from util_list import *


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        uidx = 0
        dup = 1
        i = 1
        while i < len(nums):
            if nums[uidx] == nums[i] and dup > 0:
                uidx += 1
                nums[uidx] = nums[i]
                dup -= 1
                continue
            if nums[uidx] != nums[i] or 1 == dup:
                uidx += 1
                nums[uidx] = nums[i]
                dup = 1
            i += 1
        return uidx + 1


stime = time.time()
#print(Solution().removeDuplicates([1,2,3]))
#print(Solution().removeDuplicates([1,1,1,2,2,3]))
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))
#print(Solution().removeDuplicates([1, 1, 1, 2, 3]))
print('elapse time: {} sec'.format(time.time() - stime))
