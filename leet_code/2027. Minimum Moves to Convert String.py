import time
from util.util_list import *
from util.util_tree import *
import copy
import collections
import bisect
from typing import List
import math



class Solution:
    def minimumMoves(self, s: str) -> int:
        idxs = []
        for i, ch in enumerate(s):
            if ch == 'X':
                idxs += i,
        
        cnt = 0
        
        while idxs:
            cur = idxs.pop(0)
            
            while idxs and cur + 2 >= idxs[0]:
                idxs.pop(0)
        
            cnt += 1
        
        return cnt


stime = time.time()
print(2 == Solution().minimumMoves("XXOX"))
print('elapse time: {} sec'.format(time.time() - stime))