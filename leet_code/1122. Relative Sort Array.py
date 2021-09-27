import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = collections.Counter(arr1)
        res = []

        for num in arr2:
            res += freq[num]*[num]

        arr1_nums = set(arr1) - set(arr2)
        for num in sorted(arr1_nums):
            res += freq[num]*[num]

        return res


stime = time.time()
print([2,2,2,1,4,3,3,9,6,7,19] == Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print('elapse time: {} sec'.format(time.time() - stime))