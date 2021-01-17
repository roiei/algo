import time
from util.util_list import *
from typing import List


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        l = 0
        dup = 0
        r = 1

        while r < len(nums):
            if nums[l] == nums[r]:
                if dup < 1:
                    l += 1
                    nums[l] = nums[r]
                    dup += 1
            elif nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
                dup = 0

            r += 1

        return l + 1


stime = time.time()
#print(Solution().removeDuplicates([1,2,3]))
#print(Solution().removeDuplicates([1,1,1,2,2,3]))
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))
#print(Solution().removeDuplicates([1, 1, 1, 2, 3]))
print('elapse time: {} sec'.format(time.time() - stime))
