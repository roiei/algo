
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List



class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = collections.Counter(changed)
        if freq[0]%2:
            return []

        for k in list(freq.keys()):
            if freq[k] > freq[k*2]:
                return []

            freq[k*2] -= freq[k] if k else freq[k]//2

        return list(freq.elements())


stime = time.time()
# print([1,3,4] == Solution().findOriginalArray(changed = [1,3,4,2,6,8]))
# print([] == Solution().findOriginalArray([6,3,0,1]))
# print([0,0] == Solution().findOriginalArray([0,0,0,0]))
# print([] == Solution().findOriginalArray([3,3,3,3]))
print([0,2,3] == Solution().findOriginalArray([0,3,2,4,6,0]))
print('elapse time: {} sec'.format(time.time() - stime))