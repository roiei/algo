import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(token) for token in s.split() if token.isdigit()]
        if not nums:
            return False

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                break
        else:
            return True

        return False


stime = time.time()
print(True == Solution().areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
print('elapse time: {} sec'.format(time.time() - stime))