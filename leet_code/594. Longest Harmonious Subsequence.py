
import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        mx = 0
        
        for i in freq:
            if i + 1 not in freq:
                continue
            
            mx = max(mx, freq[i + 1] + freq[i])

        return mx
        

stime = time.time()
print(5 == Solution().findLHS([1,3,2,2,5,2,3,7]))
print('elapse time: {} sec'.format(time.time() - stime))