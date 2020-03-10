import time
from util_list import *
from util_tree import *
import copy
import collections



class Solution:
    def magicalString(self, n: int) -> int:
        if 0 == n:
            return 0
        nums = [1, 2, 2]
        i = 3
        idx = 2
        while i < n:
            val = 1 if 2 == nums[-1] else 2
            nums += nums[idx]*[val]
            idx += 1
            i += 1
        return nums[:n].count(1)






stime = time.time()
print(Solution().magicalString(6))
print('elapse time: {} sec'.format(time.time() - stime))