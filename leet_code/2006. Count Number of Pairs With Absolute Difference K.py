
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List



class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = collections.Counter(nums)
        return sum(cnt[num - k] for num in nums)


stime = time.time()
print(4 == Solution().countKDifference(nums = [1,2,2,1], k = 1))
print('elapse time: {} sec'.format(time.time() - stime))