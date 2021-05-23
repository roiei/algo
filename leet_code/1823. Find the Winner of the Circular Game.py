import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


# n = 5
# k = 2
# nums = [1, 2, 3, 4, 5]
#         -
#        [1, 3, 4, 5]
#            -
#        [1, 3, 5]
#               -
#        [3, 5]
#         -
#        [3]

# n = 6, k = 5
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 6]
# ...



class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(1, n + 1))
        s = 0
        while len(nums) > 1:
            s = (s + k - 1)%len(nums)
            nums.pop(s)
            s = s%len(nums)

        return nums[0]
        

stime = time.time()
print(3 == Solution().findTheWinner(n = 5, k = 2))
print(1 == Solution().findTheWinner(n = 6, k = 5))
print('elapse time: {} sec'.format(time.time() - stime))