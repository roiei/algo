
import time
from util.util_list import *
from util.util_tree import *
import heapq
import copy
import collections
import operator


class Solution:
    def maximum69Number (self, num: int) -> int:
        
        nums = list(map(int, list(str(num))))

        for i, num in enumerate(nums):
            if num == 6:
                nums = nums[:i] + [9] + nums[i + 1:]
                return int(''.join(str(num) for num in nums))
        
        return int(''.join([str(num) for num in nums]))

            
stime = time.time()
print(9969 == Solution().maximum69Number(9669))
print('elapse time: {} sec'.format(time.time() - stime))