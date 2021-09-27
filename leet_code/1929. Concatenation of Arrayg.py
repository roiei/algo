import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums[:] + nums[:]
            

stime = time.time()
print([1,2,1,1,2,1] == Solution().getConcatenation([1,2,1]))
print('elapse time: {} sec'.format(time.time() - stime))
